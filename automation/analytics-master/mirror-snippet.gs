/* ============================================================================
 * mirror-snippet.gs  —  nối 1 kênh vào DTO Master (Looker Studio đa kênh)
 *
 * Khối code bên dưới ĐÃ CÓ SẴN trong Code.gs tuyến "Công Nghệ Số". File này để
 * copy sang Code.gs các kênh KHÁC (Kinh Tế Số, và kênh sau này).
 *
 * CÁCH DÙNG (cho Code.gs của repo bot-ban-hang-kinh-doanh / kênh khác):
 *   1. Dán TOÀN BỘ khối bên dưới vào CUỐI Code.gs của kênh đó.
 *   2. Trong hàm refreshEngagementMetrics(), ngay SAU dòng
 *          try { refreshAudienceGrowth_(); } catch (e) { ... }
 *      thêm:
 *          try { mirrorAnalyticsToMaster_(); } catch (e) { Logger.log('mirrorAnalyticsToMaster_ failed: %s', e); }
 *   3. Deploy lại "Phiên bản mới" (giữ exec URL).
 *   4. ⚙ Cài đặt dự án → Thuộc tính của tập lệnh, thêm 2 dòng:
 *          MASTER_SHEET_ID = 1isvFaqM9g6F8hFb3Fu5pvMg2Jgj017Nsh6R0OgHsof0
 *          BRAND_SLUG      = kinh_te_so
 *   5. Chạy tay refreshEngagementMetrics() 1 lần để kiểm tra master nhận dòng
 *      brand = kinh_te_so ở post_metrics + traffic_daily.
 *
 * Phụ thuộc (đều có sẵn trong Code.gs mỗi kênh): numOrZero_, getEngagementSheet_,
 * getAudienceSheet_, ENGAGEMENT_HEADERS, AUDIENCE_HEADERS.
 * ============================================================================ */

// ---- Mirror to the shared analytics master (multi-brand Looker Studio source) ----
//
// ---- Mirror to the shared analytics master (multi-brand Looker Studio source) ----
//
// After refreshEngagementMetrics + refreshAudienceGrowth_ update THIS channel's own
// sheet, copy the numbers into a shared master workbook so ONE Looker Studio report
// can break "organic traffic" down by content brand (kinh_te_so / cong_nghe_so / …)
// and also roll up an "all channels" total. Same function drops into every channel's
// Code.gs unchanged — it only needs two Script Properties per channel:
//   MASTER_SHEET_ID  — the master spreadsheet's file id (same value in every channel)
//   BRAND_SLUG       — this channel's brand key, e.g. "cong_nghe_so"
// If either is missing the function no-ops (channel not wired to the master yet).
//
// NOTE ON NAMING: this channel's own sheet calls the platform column "channel"
// (facebook/instagram/youtube/threads). The master keeps that as `platform` and adds
// a separate `brand` column — so "channel" is never ambiguous in the report. Values in
// BOTH master columns are written HUMAN-READABLE ("Công Nghệ Số", "Facebook", "YouTube")
// so the raw sheet + Looker read nicely without a lookup (user request 08/09/2026).
// BRAND_SLUG stays the machine key in Script Properties; it's mapped on write.
//
// Master tabs written (created by setupMaster() in automation/analytics-master/):
//   post_metrics   — upsert 1 row per (brand, post_id): current per-post numbers
//   traffic_daily  — upsert 1 row per (brand, platform, date): that day's totals
//                    + *_delta vs the previous day = the organic traffic gained that day
var MASTER_POST_METRICS_HEADERS = [
  'brand', 'platform', 'video_project', 'post_type', 'post_id', 'permalink', 'title',
  'posted_at', 'posted_date', 'views', 'likes', 'reactions', 'comments', 'shares', 'last_checked'
];
var MASTER_TRAFFIC_DAILY_HEADERS = [
  'brand', 'platform', 'date', 'posts_published',
  'views_total', 'views_delta', 'engagement_total', 'engagement_delta',
  'followers', 'followers_delta'
];
var MASTER_BRAND_DISPLAY = {
  kinh_te_so: 'Kinh Tế Số', cong_nghe_so: 'Công Nghệ Số', tin_tuc_so: 'Tin Tức Số',
  ai_marketing: 'AI Marketing', marketing_online: 'Marketing Online'
};
var MASTER_PLATFORM_DISPLAY = {
  facebook: 'Facebook', instagram: 'Instagram', youtube: 'YouTube', threads: 'Threads'
};
function masterPlatformName_(v) {
  var k = String(v || '').toLowerCase().trim();
  return MASTER_PLATFORM_DISPLAY[k] || (k ? k.charAt(0).toUpperCase() + k.slice(1) : '');
}

function mirrorAnalyticsToMaster_() {
  var props = PropertiesService.getScriptProperties();
  var masterId = props.getProperty('MASTER_SHEET_ID');
  var brandSlug = props.getProperty('BRAND_SLUG');
  if (!masterId || !brandSlug) {
    Logger.log('mirrorAnalyticsToMaster_: MASTER_SHEET_ID / BRAND_SLUG not set — skipping');
    return;
  }
  var brand = MASTER_BRAND_DISPLAY[brandSlug] || brandSlug; // human-readable, used as the key
  var master = SpreadsheetApp.openById(masterId);
  var tz = 'Asia/Ho_Chi_Minh';
  var today = Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd');
  var asDate_ = function (v) {
    return v instanceof Date ? Utilities.formatDate(v, tz, 'yyyy-MM-dd') : String(v || '').slice(0, 10);
  };

  // --- this channel's freshly-refreshed engagement_metrics rows ---
  var engSheet = getEngagementSheet_();
  var engRows = [];
  if (engSheet.getLastRow() > 1) {
    engSheet.getRange(2, 1, engSheet.getLastRow() - 1, ENGAGEMENT_HEADERS.length).getValues()
      .forEach(function (r) {
        var rec = {}; ENGAGEMENT_HEADERS.forEach(function (h, i) { rec[h] = r[i]; });
        if (!rec.platform_post_id) return;
        rec._platform = masterPlatformName_(rec.channel); // "Facebook" (from "facebook"/"Facebook")
        engRows.push(rec);
      });
  }

  // --- upsert post_metrics (key: brand|post_id) ---
  var pm = master.getSheetByName('post_metrics');
  if (pm) {
    var pmVals = pm.getLastRow() > 1
      ? pm.getRange(2, 1, pm.getLastRow() - 1, MASTER_POST_METRICS_HEADERS.length).getValues() : [];
    var pmRowByKey = {};
    pmVals.forEach(function (r, i) { pmRowByKey[r[0] + '|' + r[4]] = i + 2; });
    engRows.forEach(function (rec) {
      var row = [
        brand, rec._platform, rec.video_project, rec.post_type, rec.platform_post_id,
        rec.permalink, rec.title, rec.posted_at, rec.posted_date,
        numOrZero_(rec.views), numOrZero_(rec.likes), numOrZero_(rec.reactions),
        numOrZero_(rec.comments), numOrZero_(rec.shares), rec.last_checked
      ];
      var at = pmRowByKey[brand + '|' + rec.platform_post_id];
      if (at) pm.getRange(at, 1, 1, row.length).setValues([row]);
      else pm.appendRow(row);
    });
  }

  // --- latest follower count per platform, from this channel's audience_growth ---
  var followersByPlatform = {};
  var aud = getAudienceSheet_();
  if (aud.getLastRow() > 1) {
    var chIdx = AUDIENCE_HEADERS.indexOf('channel');
    var fIdx = AUDIENCE_HEADERS.indexOf('followers');
    var dIdx = AUDIENCE_HEADERS.indexOf('date');
    aud.getRange(2, 1, aud.getLastRow() - 1, AUDIENCE_HEADERS.length).getValues().forEach(function (r) {
      var p = masterPlatformName_(r[chIdx]);
      if (!p) return;
      var d = asDate_(r[dIdx]);
      if (!followersByPlatform[p] || d >= followersByPlatform[p].date) {
        followersByPlatform[p] = { date: d, followers: numOrZero_(r[fIdx]) };
      }
    });
  }

  // --- aggregate today's totals per platform ---
  var byPlatform = {};
  engRows.forEach(function (rec) {
    var p = rec._platform; if (!p) return;
    byPlatform[p] = byPlatform[p] || { views: 0, eng: 0, postsToday: 0 };
    byPlatform[p].views += numOrZero_(rec.views);
    byPlatform[p].eng += numOrZero_(rec.likes) + numOrZero_(rec.reactions)
      + numOrZero_(rec.comments) + numOrZero_(rec.shares);
    if (asDate_(rec.posted_date) === today) byPlatform[p].postsToday++;
  });
  Object.keys(followersByPlatform).forEach(function (p) {
    byPlatform[p] = byPlatform[p] || { views: 0, eng: 0, postsToday: 0 };
  });

  // --- upsert traffic_daily (key: brand|platform|today), deltas vs previous day ---
  var td = master.getSheetByName('traffic_daily');
  if (td) {
    var tdVals = td.getLastRow() > 1
      ? td.getRange(2, 1, td.getLastRow() - 1, MASTER_TRAFFIC_DAILY_HEADERS.length).getValues() : [];
    Object.keys(byPlatform).forEach(function (p) {
      var agg = byPlatform[p];
      var f = followersByPlatform[p] ? followersByPlatform[p].followers : '';
      var prev = null, todayRow = null;
      tdVals.forEach(function (r, i) {
        if (String(r[0]) !== brand || masterPlatformName_(r[1]) !== p) return;
        var rd = asDate_(r[2]);
        if (rd === today) todayRow = i + 2;
        else if (rd < today && (!prev || rd > prev.d)) {
          prev = { d: rd, views: numOrZero_(r[4]), eng: numOrZero_(r[6]), followers: r[8] };
        }
      });
      var row = [
        brand, p, today, agg.postsToday,
        agg.views, prev ? agg.views - prev.views : '',
        agg.eng, prev ? agg.eng - prev.eng : '',
        f, (prev && f !== '' && prev.followers !== '' && !isNaN(prev.followers)) ? f - Number(prev.followers) : ''
      ];
      if (todayRow) td.getRange(todayRow, 1, 1, row.length).setValues([row]);
      else td.appendRow(row);
    });
  }

  Logger.log('mirrorAnalyticsToMaster_: brand=%s platforms=[%s]', brand, Object.keys(byPlatform).join(','));
}
