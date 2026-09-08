/**
 * DTO Master — DATA TRAFFIC ORGANIC, nguồn dữ liệu chung cho Looker Studio.
 *
 * Gắn (bound) vào file "Bản sao của BBH News Queue" qua Tiện ích mở rộng →
 * Apps Script. Chạy MỘT LẦN `setupMaster()` để:
 *   1. tạo 3 tab mới: brands / post_metrics / traffic_daily (+ header)
 *   2. seed bảng `brands`
 *   3. di trú dữ liệu cũ của Kinh Tế Số:
 *        engagement_metrics  → post_metrics   (brand = kinh_te_so)
 *        audience_growth     → traffic_daily  (brand = kinh_te_so, cột followers + delta)
 *
 * KHÔNG xoá tab cũ (engagement_metrics / audience_growth / posts_log / news_queue) —
 * người dùng muốn giữ lại bản chụp lịch sử. Sau khi các Apps Script kênh (Kinh Tế
 * Số + Công Nghệ Số) chạy `mirrorAnalyticsToMaster_()` vài ngày, nếu số liệu cũ đã
 * được cập nhật lại đầy đủ trong post_metrics thì có thể xoá 2 tab cũ thủ công.
 *
 * File này KHÔNG cần trigger — mỗi Apps Script kênh tự đẩy dữ liệu sang (xem
 * `mirrorAnalyticsToMaster_` trong automation/news-fetch-gas/Code.gs).
 */

var BRANDS_SHEET = 'brands';
var POST_METRICS_SHEET = 'post_metrics';
var TRAFFIC_DAILY_SHEET = 'traffic_daily';

// Header hàng 1 = tiếng Việt, viết hoa chữ cái đầu câu (yêu cầu người dùng 08/09/2026).
// Toàn bộ code (mirror + migrate) truy cột theo VỊ TRÍ, không theo tên header, nên đổi
// nhãn hàng 1 không ảnh hưởng — chỉ KHÔNG được đổi thứ tự cột.
// Giá trị cột "Kênh" / "Nền tảng" ghi DẠNG NGƯỜI ĐỌC (viết hoa chữ đầu) — yêu cầu người dùng
// 08/09/2026. Đây cũng là khoá join giữa các tab + với Looker. `BRAND_SLUG` (Script Property của
// từng kênh) vẫn là khoá máy, được map sang tên hiển thị khi ghi.
var BRAND_DISPLAY = {
  kinh_te_so: 'Kinh Tế Số', cong_nghe_so: 'Công Nghệ Số', tin_tuc_so: 'Tin Tức Số',
  ai_marketing: 'AI Marketing', marketing_online: 'Marketing Online'
};
var PLATFORM_DISPLAY = {
  facebook: 'Facebook', instagram: 'Instagram', youtube: 'YouTube', threads: 'Threads'
};
function platformName_(v) {
  var k = String(v || '').toLowerCase().trim();
  return PLATFORM_DISPLAY[k] || (k ? k.charAt(0).toUpperCase() + k.slice(1) : '');
}
function brandName_(v) {
  var s = String(v || '').trim();
  return BRAND_DISPLAY[s] || s;
}

var BRANDS_HEADERS = ['Mã kênh', 'Tên kênh', 'Biểu tượng', 'Thứ tự', 'Đang hoạt động'];
var BRANDS_SEED = [
  ['Kinh Tế Số',   'Kinh Tế Số',   '📊', 1, true],
  ['Công Nghệ Số', 'Công Nghệ Số', '💻', 2, true],
  ['Tin Tức Số',   'Tin Tức Số',   '📰', 3, true]
  // ['AI Marketing',     'AI Marketing',     '🤖', 4, false],   // bật khi dựng kênh
  // ['Marketing Online', 'Marketing Online', '📈', 5, false],
];

var POST_METRICS_HEADERS = [
  'Kênh', 'Nền tảng', 'Dự án video', 'Loại bài đăng', 'Mã bài đăng', 'Liên kết', 'Tiêu đề',
  'Thời gian đăng', 'Ngày đăng', 'Lượt xem', 'Lượt thích', 'Cảm xúc', 'Bình luận', 'Lượt chia sẻ',
  'Lần kiểm tra cuối'
];
var TRAFFIC_DAILY_HEADERS = [
  'Kênh', 'Nền tảng', 'Ngày', 'Số bài đăng',
  'Tổng lượt xem', 'Lượt xem tăng thêm', 'Tổng tương tác', 'Tương tác tăng thêm',
  'Người theo dõi', 'Người theo dõi tăng thêm'
];

// Legacy tab (bản copy từ BBH News Queue) — chỉ đọc để di trú + đổi nhãn hàng 1.
// Thứ tự cột legacy (positional, KHÔNG đọc tên header thật).
var LEGACY_ENGAGEMENT_SHEET = 'engagement_metrics';
var LEGACY_ENGAGEMENT_HEADERS = [
  'channel', 'video_project', 'post_type', 'platform_post_id', 'permalink',
  'title', 'posted_at', 'posted_date', 'posted_time',
  'views', 'likes', 'reactions', 'comments', 'shares', 'last_checked', 'notes'
];
var LEGACY_AUDIENCE_SHEET = 'audience_growth';
var LEGACY_AUDIENCE_HEADERS = ['channel', 'checked_at', 'date', 'time', 'followers', 'notes'];

// Nhãn hàng 1 tiếng Việt cho các tab legacy (đổi 1 lần qua relabelHeaders()).
var LEGACY_LABELS = {
  'engagement_metrics': ['Kênh', 'Dự án video', 'Loại bài đăng', 'Mã bài đăng', 'Liên kết bài đăng',
    'Tiêu đề', 'Thời gian đăng (UTC)', 'Ngày đăng', 'Giờ đăng', 'Lượt xem', 'Lượt thích', 'Cảm xúc',
    'Bình luận', 'Lượt chia sẻ', 'Lần kiểm tra cuối', 'Ghi chú'],
  'audience_growth': ['Kênh', 'Thời gian kiểm tra', 'Ngày', 'Giờ', 'Người theo dõi', 'Ghi chú'],
  'posts_log': ['Thời gian đăng', 'Nền tảng', 'Loại bài đăng', 'Dự án video', 'Tiêu đề', 'Nội dung',
    'Mã bài đăng', 'Liên kết', 'Trạng thái', 'Người đăng', 'Ghi chú'],
  'news_queue': ['Mã', 'Tiêu đề', 'Liên kết', 'Nguồn', 'Phân loại', 'Ngày xuất bản', 'Ngày lấy về',
    'Đã dùng', 'Thời điểm dùng', 'Video dùng', 'Liên kết ảnh', 'Mã tệp ảnh']
};

var LEGACY_BRAND = 'Kinh Tế Số'; // toàn bộ dữ liệu cũ trong file thuộc kênh Kinh Tế Số
var TZ = 'Asia/Ho_Chi_Minh';

function setupMaster() {
  var ss = SpreadsheetApp.getActive();
  var created = [];

  ensureSheetWithHeaders_(ss, BRANDS_SHEET, BRANDS_HEADERS, created);
  var brandsSheet = ss.getSheetByName(BRANDS_SHEET);
  if (brandsSheet.getLastRow() < 2) {
    brandsSheet.getRange(2, 1, BRANDS_SEED.length, BRANDS_HEADERS.length).setValues(BRANDS_SEED);
  }

  ensureSheetWithHeaders_(ss, POST_METRICS_SHEET, POST_METRICS_HEADERS, created);
  ensureSheetWithHeaders_(ss, TRAFFIC_DAILY_SHEET, TRAFFIC_DAILY_HEADERS, created);

  var norm = normalizeValues_(ss); // slug -> tên hiển thị TRƯỚC khi migrate (tránh trùng dòng)
  var migPost = migrateLegacyEngagement_(ss);
  var migTraffic = migrateLegacyAudience_(ss);
  var relabeled = relabelHeaders_(ss);

  var msg = 'setupMaster xong.\n'
    + 'Tab tạo mới: ' + (created.length ? created.join(', ') : '(đã có sẵn)') + '\n'
    + 'brands: ' + BRANDS_SEED.length + ' dòng\n'
    + 'Chuẩn hoá tên Kênh/Nền tảng: ' + norm + ' ô\n'
    + 'Di trú post_metrics (Kinh Tế Số): ' + migPost + ' dòng\n'
    + 'Di trú traffic_daily follower history (Kinh Tế Số): ' + migTraffic + ' dòng\n'
    + 'Đổi nhãn hàng 1 (tiếng Việt): ' + relabeled.join(', ');
  Logger.log(msg);
  try { SpreadsheetApp.getUi().alert(msg); } catch (e) { /* chạy không có UI */ }
  return msg;
}

/**
 * Chạy độc lập (không cần setupMaster) để đổi hàng 1 mọi tab sang nhãn tiếng Việt.
 * An toàn để chạy lại — chỉ ghi đè hàng 1, không đụng dữ liệu.
 */
function relabelHeaders() {
  var ss = SpreadsheetApp.getActive();
  var done = relabelHeaders_(ss);
  var msg = 'Đã đổi nhãn hàng 1 sang tiếng Việt: ' + done.join(', ');
  Logger.log(msg);
  try { SpreadsheetApp.getUi().alert(msg); } catch (e) {}
  return msg;
}

/**
 * Chạy độc lập: viết hoa / chuẩn hoá giá trị cột "Kênh" + "Nền tảng" trong post_metrics,
 * traffic_daily (và cột "Mã kênh" của brands) sang dạng người đọc — facebook -> Facebook,
 * kinh_te_so -> Kinh Tế Số. An toàn để chạy lại (idempotent).
 */
function normalizeValues() {
  var ss = SpreadsheetApp.getActive();
  var n = normalizeValues_(ss);
  var msg = 'Đã chuẩn hoá ' + n + ' ô tên Kênh / Nền tảng sang dạng viết hoa (Facebook, Kinh Tế Số...).';
  Logger.log(msg);
  try { SpreadsheetApp.getUi().alert(msg); } catch (e) {}
  return msg;
}

function normalizeValues_(ss) {
  var changed = 0;
  // post_metrics: cột A = Kênh, cột B = Nền tảng
  changed += normalizeCols_(ss.getSheetByName(POST_METRICS_SHEET), [
    { col: 1, fn: brandName_ }, { col: 2, fn: platformName_ }
  ]);
  // traffic_daily: cột A = Kênh, cột B = Nền tảng
  changed += normalizeCols_(ss.getSheetByName(TRAFFIC_DAILY_SHEET), [
    { col: 1, fn: brandName_ }, { col: 2, fn: platformName_ }
  ]);
  // brands: cột A = Mã kênh (khoá join)
  changed += normalizeCols_(ss.getSheetByName(BRANDS_SHEET), [{ col: 1, fn: brandName_ }]);
  return changed;
}

function normalizeCols_(sh, specs) {
  if (!sh || sh.getLastRow() < 2) return 0;
  var n = sh.getLastRow() - 1;
  var changed = 0;
  specs.forEach(function (s) {
    var rng = sh.getRange(2, s.col, n, 1);
    var vals = rng.getValues();
    var dirty = false;
    for (var i = 0; i < vals.length; i++) {
      var v = vals[i][0];
      if (v === '' || v === null) continue;
      var nv = s.fn(v);
      if (nv !== v) { vals[i][0] = nv; dirty = true; changed++; }
    }
    if (dirty) rng.setValues(vals);
  });
  return changed;
}

function relabelHeaders_(ss) {
  var done = [];
  var apply = function (name, labels) {
    var sh = ss.getSheetByName(name);
    if (!sh) return;
    sh.getRange(1, 1, 1, labels.length).setValues([labels]);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, labels.length).setFontWeight('bold');
    done.push(name);
  };
  apply(BRANDS_SHEET, BRANDS_HEADERS);
  apply(POST_METRICS_SHEET, POST_METRICS_HEADERS);
  apply(TRAFFIC_DAILY_SHEET, TRAFFIC_DAILY_HEADERS);
  Object.keys(LEGACY_LABELS).forEach(function (name) { apply(name, LEGACY_LABELS[name]); });
  return done;
}

function ensureSheetWithHeaders_(ss, name, headers, createdOut) {
  var sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    if (createdOut) createdOut.push(name);
  }
  var have = sh.getLastColumn() >= headers.length
    ? sh.getRange(1, 1, 1, headers.length).getValues()[0] : [];
  var same = have.length === headers.length && have.every(function (v, i) { return v === headers[i]; });
  if (!same) {
    sh.getRange(1, 1, 1, headers.length).setValues([headers]);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, headers.length).setFontWeight('bold');
  }
  return sh;
}

function migrateLegacyEngagement_(ss) {
  var src = ss.getSheetByName(LEGACY_ENGAGEMENT_SHEET);
  var dst = ss.getSheetByName(POST_METRICS_SHEET);
  if (!src || src.getLastRow() < 2) return 0;

  var rows = src.getRange(2, 1, src.getLastRow() - 1, LEGACY_ENGAGEMENT_HEADERS.length).getValues();
  var col = {};
  LEGACY_ENGAGEMENT_HEADERS.forEach(function (h, i) { col[h] = i; });

  // upsert theo key brand|post_id để chạy lại setupMaster không tạo trùng
  // (brandName_ chuẩn hoá cả dòng cũ còn slug lẫn dòng mới đã là tên hiển thị)
  var existing = {};
  if (dst.getLastRow() > 1) {
    dst.getRange(2, 1, dst.getLastRow() - 1, POST_METRICS_HEADERS.length).getValues()
      .forEach(function (r, i) { existing[brandName_(r[0]) + '|' + r[4]] = i + 2; });
  }

  var out = [];
  rows.forEach(function (r) {
    var postId = String(r[col.platform_post_id] || '').trim();
    if (!postId) return;
    var platform = platformName_(r[col.channel]);
    var row = [
      LEGACY_BRAND, platform, r[col.video_project], r[col.post_type], postId,
      r[col.permalink], r[col.title], r[col.posted_at], r[col.posted_date],
      numOrZero_(r[col.views]), numOrZero_(r[col.likes]), numOrZero_(r[col.reactions]),
      numOrZero_(r[col.comments]), numOrZero_(r[col.shares]), r[col.last_checked]
    ];
    var at = existing[LEGACY_BRAND + '|' + postId];
    if (at) dst.getRange(at, 1, 1, row.length).setValues([row]);
    else out.push(row);
  });
  if (out.length) dst.getRange(dst.getLastRow() + 1, 1, out.length, POST_METRICS_HEADERS.length).setValues(out);
  return rows.length;
}

function migrateLegacyAudience_(ss) {
  var src = ss.getSheetByName(LEGACY_AUDIENCE_SHEET);
  var dst = ss.getSheetByName(TRAFFIC_DAILY_SHEET);
  if (!src || src.getLastRow() < 2) return 0;

  var rows = src.getRange(2, 1, src.getLastRow() - 1, LEGACY_AUDIENCE_HEADERS.length).getValues();
  var col = {};
  LEGACY_AUDIENCE_HEADERS.forEach(function (h, i) { col[h] = i; });

  // (platform, date) -> followers, chọn dòng mới nhất nếu trùng ngày
  var byKey = {};
  rows.forEach(function (r) {
    var platform = platformName_(r[col.channel]);
    var d = asDate_(r[col.date]);
    if (!platform || !d) return;
    byKey[platform + '|' + d] = numOrZero_(r[col.followers]);
  });

  // sắp theo platform + date để tính followers_delta
  var keys = Object.keys(byKey).sort();
  var lastByPlatform = {};
  var out = [];

  // upsert theo key brand|platform|date
  var existing = {};
  if (dst.getLastRow() > 1) {
    dst.getRange(2, 1, dst.getLastRow() - 1, TRAFFIC_DAILY_HEADERS.length).getValues()
      .forEach(function (r, i) { existing[brandName_(r[0]) + '|' + platformName_(r[1]) + '|' + asDate_(r[2])] = i + 2; });
  }

  keys.forEach(function (k) {
    var parts = k.split('|');
    var platform = parts[0], d = parts[1];
    var followers = byKey[k];
    var prev = lastByPlatform[platform];
    var delta = (prev === undefined) ? '' : followers - prev;
    lastByPlatform[platform] = followers;

    // cột metric bài đăng để trống cho dòng lịch sử (chỉ có follower history)
    var row = [LEGACY_BRAND, platform, d, '', '', '', '', '', followers, delta];
    var at = existing[LEGACY_BRAND + '|' + platform + '|' + d];
    if (at) dst.getRange(at, 1, 1, row.length).setValues([row]);
    else out.push(row);
  });
  if (out.length) dst.getRange(dst.getLastRow() + 1, 1, out.length, TRAFFIC_DAILY_HEADERS.length).setValues(out);
  return keys.length;
}

function numOrZero_(v) { return (v === '' || v === undefined || v === null || isNaN(v)) ? 0 : Number(v); }
function asDate_(v) {
  return v instanceof Date ? Utilities.formatDate(v, TZ, 'yyyy-MM-dd') : String(v || '').slice(0, 10);
}
