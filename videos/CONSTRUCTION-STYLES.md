# 10 cách dựng (Construction Styles) — TIN TỨC SỐ

Danh mục "hệ ngôn ngữ hình ảnh" để xoay vòng giữa các video, tránh lặp bố cục. Đọc song song với
`BRAND-SYSTEM.md` (màu / font / 7 act cố định) và `PRODUCTION-WORKFLOW.md` (quy trình).

Cùng bộ 10 slot với các tuyến khác (Apps Script `STYLE_ROTATION` cấp qua `claim_style` dưới
LockService), nhưng ẩn dụ được **diễn giải lại cho tin nóng / trending trong ngày** (mọi chủ đề,
không riêng công nghệ).

## Phạm vi áp dụng

Mỗi video 7 act: Hook · What happened · Key facts · Data moment · Context · Impact · **CTA**.

- **Hook (act 1), Brand Anchor (logo + tên kênh góc trên-phải, nguồn góc trên-trái), và act 7 CTA
  LUÔN CỐ ĐỊNH** ở mọi style. Hook = title-card (masthead → badge nguồn + ngày → tên chủ thể TO →
  2 tag tương phản). CTA = câu hỏi tranh luận + 2 lựa chọn đối lập + pill "Bình luận quan điểm của
  bạn" + chữ ký logo.
- **5 act giữa (What happened / Key facts / Data moment / Context / Impact) đổi thiết bị hình ảnh
  theo style** — đây là phần tạo cảm giác "mỗi video một kiểu".

## Cơ chế xoay vòng

Con trỏ thật ở Apps Script (Script Property `STYLE_CURSOR`), cấp qua `POST {"action":"claim_style"}`.
`videos/style-rotation-state.json` chỉ là bản sao cho người đọc — vẫn thêm 1 dòng `log` mỗi video.

## Bảng 10 style

| # | slug | Ẩn dụ (tech) |
| - | --- | --- |
| 0 | `1-card-and-bar` | Thẻ thông số bo góc + cột so sánh dọc (benchmark, spec) |
| 1 | `2-chip-and-leaderboard` | Chip số liệu viền cam + bảng xếp hạng model/hãng, watermark số khổng lồ |
| 2 | `3-ticker-tape` | Dải "release feed / changelog" chạy ngang kiểu terminal |
| 3 | `4-split-comparison` | Chia đôi khung: model cũ ↔ mới, hãng A ↔ B, trước ↔ sau |
| 4 | `5-map-and-geo` | Bản đồ — địa lý sự kiện (vùng chịu ảnh hưởng, tỉnh/thành, quốc gia liên quan) |
| 5 | `6-ring-progress` | Vòng tiến trình radial — % benchmark, tỉ lệ chấp nhận, thị phần |
| 6 | `7-timeline-chronology` | Trục thời gian — lộ trình phát hành, các đời model, mốc phát triển |
| 7 | `8-icon-grid` | Lưới ô tính năng / nền tảng / lĩnh vực áp dụng |
| 8 | `9-editorial-clipping` | Mảnh báo cắt dán chồng lớp, dấu ngoặc kép lớn — trích phát ngôn lãnh đạo hãng |
| 9 | `10-stock-terminal` | Bảng benchmark / biểu đồ hiệu năng kiểu terminal, sparkline |

## Style 0 — Card & Bar

- **What happened**: ảnh bài báo trong card + panel tối chứa kicker + 1–2 câu chốt "chuyện gì".
- **Key facts**: mỗi fact là 1 thẻ bo góc có số thứ tự nhỏ góc trái, reveal slide/mask lần lượt.
- **Data moment**: con số chính TO ở giữa, bên dưới là 2–3 cột dọc ngắn so sánh (vd điểm benchmark
  của A vs B vs C) — cột count-up cao dần, số chính là cột cao nhất được tô cam.
- **Context**: bảng 3–4 dòng thông số (nhãn trái / giá trị phải), đường kẻ mảnh phân dòng.
- **Impact**: 2 thẻ lớn cạnh nhau, mỗi thẻ 1 ý tác động, icon CSS nhỏ phía trên tiêu đề thẻ.

## Style 1 — Chip & Leaderboard

- **What happened**: ảnh + panel, thêm 2 chip số liệu viền cam (vd "3/9/2026" · "trong 1 tuần").
- **Key facts**: watermark 1 con số khổng lồ mờ phía sau (opacity thấp), 3 fact xếp dọc phía trước.
- **Data moment**: bảng xếp hạng ngang 3–5 hàng (model / hãng bên trái, thanh + số bên phải), hàng
  của chủ thể tin tô cam, thanh chạy count-up.
- **Context**: 2–3 chip lớn xếp dọc, mỗi chip 1 dữ kiện nền, viền cam, số nổi bật.
- **Impact**: 2 chip tác động lớn, watermark số mờ tiếp tục phía sau để liền mạch với act trước.

## Style 2 — Ticker Tape (release feed)

- **What happened**: ảnh nền mờ + 1 dải ngang viền trên/dưới cam chạy full-width chứa nguồn + tiêu
  đề rút gọn, 1 chấm nhấp nháy đầu dải kiểu "LIVE". Headline chính nằm phía trên dải.
- **Key facts**: mỗi fact hiện dạng dòng terminal — prefix `>` hoặc `+`, reveal typewriter từng ký tự.
- **Data moment**: con số chính giữa 2 vạch kẻ ngang mảnh, phía trên là 1 "mã" ngắn viết hoa (2–4
  ký tự gợi tên sản phẩm / hãng) chạy trước khi số count-up.
- **Context**: dải sparkline mảnh (zig-zag, không trục) chạy phía sau mỗi dòng so sánh, vẽ draw-in.
- **Impact**: 2–3 "dòng feed" xếp chồng, mỗi dòng nhãn trái + số/kết quả phải + dấu tăng/giảm
  (tam giác CSS cam/đỏ), cách nhau bằng kẻ mảnh.

## Style 3 — Split Comparison

- **What happened**: chia dọc 2 nửa — trái ảnh bài báo, phải panel tối chứa kicker + tiêu đề, vạch
  phân cách cam mảnh dọc giữa.
- **Key facts**: mỗi fact 1 hàng chia đôi — nhãn trái (nhỏ, xám), giá trị phải (lớn, trắng/cam)
  căn phải, vạch dọc mảnh giữa hàng.
- **Data moment**: 2 con số cạnh nhau qua vạch "→" hoặc "vs" giữa — số trái mờ/nhỏ (đời cũ/nền),
  số phải lớn/cam (mới/chính), vạch giữa pulse khi 2 số xuất hiện.
- **Context**: bảng 2 cột đối xứng ("trước" / "nay" hoặc "hãng A" / "hãng B"), mỗi hàng reveal đồng
  thời từ 2 phía vào giữa.
- **Impact**: chia đôi NGANG (trên/dưới, đổi nhịp so với act 2), mỗi nửa 1 ý tác động.

## Style 4 — Map & Geo

Dùng khi tin có yếu tố địa lý rõ (vùng chịu ảnh hưởng, tỉnh/thành, quốc gia liên quan
khu vực, lệnh cấm, thị trường theo nước).

- **What happened**: ảnh + badge nguồn chuẩn, thêm 1 ghim địa danh nhỏ (dot + label) chỉ vị trí
  liên quan tin.
- **Key facts**: bản đồ (khu vực / thế giới / VN tuỳ tin) vector outline mờ phía sau danh sách fact;
  fact liên quan địa lý có icon ghim nhỏ.
- **Data moment**: con số chính trong 1 map-pin phóng to, pin drop-in (bounce nhẹ) trước khi số count-up.
- **Context**: bản đồ với 3–5 vùng/nước highlight tuần tự (tô cam đậm dần theo thứ hạng), đường nối
  từ vùng ra nhãn số liệu.
- **Impact**: 2 "thẻ địa danh" trượt vào từ 2 hướng, mỗi thẻ icon ghim + tên vùng + số tác động,
  nền bản đồ mờ full-frame.

## Style 5 — Ring Progress

Nhấn tỉ lệ %: điểm benchmark, tỉ lệ chấp nhận, thị phần, mức hoàn thành roadmap.

- **What happened**: chuẩn ảnh + panel, badge nguồn đổi thành vòng tròn nhỏ viền cam bao icon nguồn.
- **Key facts**: mỗi fact có 1 mini-radial (~80px) bên trái tự vẽ đầy theo % liên quan (hoặc 100%
  nếu fact không phải %), text fact bên phải.
- **Data moment**: con số chính giữa 1 vòng radial khổng lồ, vòng vẽ đầy đồng bộ với count-up —
  ẩn dụ trung tâm của style.
- **Context**: 3–4 vòng radial cỡ vừa xếp hàng ngang, % dưới mỗi vòng, vẽ đầy tuần tự trái→phải.
- **Impact**: 2 vòng radial lớn cạnh nhau, nhãn + số ở tâm mỗi vòng.

## Style 6 — Timeline Chronology

Tin có diễn biến qua nhiều mốc: các đời model, lộ trình rollout, lịch sử một dự án.

- **What happened**: chuẩn ảnh + panel, thêm 1 badge mốc thời gian nhỏ cạnh kicker.
- **Key facts**: 3 fact xếp dọc theo 1 trục đứng bên trái (đường kẻ dọc + node tròn, node "nở" khi
  fact xuất hiện).
- **Data moment**: con số chính tại 1 node lớn trên trục NGANG giữa khung, trục vẽ dần trái→phải rồi
  dừng tại node khi số chốt.
- **Context**: trục thời gian đầy đủ 4–5 mốc (node + nhãn năm/phiên bản/mốc, giá trị đi kèm), node
  sau đậm/to hơn nếu số liệu tăng dần. **Trên canvas dọc 1080×1920, dựng trục THEO CHIỀU DỌC** (trục
  ngang thật sự chật hẹp trên khung 1080px hẹp) — xem code thật + kỹ thuật "trục vẽ dần theo scaleY"
  ở mục 6.5 của `TECHNICAL-CONSTRUCTION-GUIDE.md`. "Ngang/dọc" ở đây chỉ là hướng trục, không đổi
  ẩn dụ timeline.
- **Impact**: 2 node cuối trục phóng to thành 2 khối tác động, vẫn giữ đường trục phía sau.

## Style 7 — Icon Grid

Tin có nhiều nhóm / nền tảng / lĩnh vực áp dụng cần liệt kê song song.

- **What happened**: chuẩn ảnh + panel, 2 chip đổi thành 2 ô vuông nhỏ có icon CSS phía trên số liệu.
- **Key facts**: 3 fact thành 3 ô trong lưới 1×3 hoặc 3×1, mỗi ô 1 icon đại diện (không dùng số
  thứ tự), border mảnh.
- **Data moment**: con số chính trong 1 ô lớn giữa lưới 3 ô (2 ô phụ 2 bên mờ/nhỏ chứa số bổ trợ).
- **Context**: lưới 2×2 hoặc 2×3 ô icon + số liệu xuất hiện tuần tự theo hàng — mô phỏng dashboard.
- **Impact**: lưới 2 ô lớn cạnh nhau, icon lớn phía trên tiêu đề mỗi ô.

## Style 8 — Editorial Clipping

Cảm giác "biên tập", chồng lớp — mạnh khi tin xoay quanh phát ngôn của lãnh đạo hãng.

- **What happened**: ảnh bài báo đặt lệch (xoay nhẹ 1–2°) như mẩu báo cắt dán, viền trắng mỏng, panel
  tối bên dưới có dấu ngoặc kép lớn mờ phía sau tiêu đề.
- **Key facts**: 3 fact như 3 "mẩu giấy" xếp chồng lệch (mỗi mẩu xoay góc khác, bóng nhẹ).
- **Data moment**: con số chính có dấu ngoặc kép khổng lồ mờ phía sau, gạch chân tay-vẽ (path không
  đều) dưới con số.
- **Context**: dòng so sánh trình bày như pull-quote block, mỗi dòng gạch đầu dòng kiểu "clipping".
- **Impact**: 2 "mẩu báo" chồng lên nhau một phần, mỗi mẩu 1 tác động — chiều sâu vật lý.

## Style 9 — Stock Terminal (benchmark board)

Tin thuần số liệu hiệu năng / benchmark / giá.

- **What happened**: chuẩn ảnh + panel, thêm 1 dải "mã hiệu năng" nhỏ dưới badge nguồn (texture
  trang trí, không phải nội dung thật).
- **Key facts**: mỗi fact có 1 icon cột mini (bar/candlestick) cạnh số thứ tự, cột "nở" cao/thấp
  theo tính tăng/giảm của fact.
- **Data moment**: con số chính có 1 đường line-chart nhỏ chạy ngang phía sau, vẽ dần trái→phải,
  chạm đỉnh đúng lúc số count-up chốt.
- **Context**: biểu đồ cột đầy đủ 4–6 cột (cam / đỏ), mỗi cột có nhãn số phía trên.
- **Impact**: 2 sparkline ngang xếp chồng, đường vẽ xong thì số cuối dòng mới hiện.

## Nguyên tắc chung cho mọi style (bắt buộc)

- Tuân thủ TOÀN BỘ `BRAND-SYSTEM.md`: màu `#FF5A1F` / `#0B0E14` / `#FF4438`, Montserrat mọi vai trò,
  sentence case, WCAG AA, Brand Anchor cố định góc trên, Hook + act 7 CTA cố định, act 6 nội dung là
  sự thật (không suy đoán tương lai).
- Mỗi style là **ẩn dụ hình ảnh**, KHÔNG phải màu mới — Stock Terminal / Ticker KHÔNG dùng xanh lá
  cho "tăng", vẫn dùng `#FF5A1F` cho điểm nhấn tích cực, `#FF4438` cho rủi ro / mặt "mối lo".
- KHÔNG emoji trong composition — icon = CSS shapes / SVG.
- Mô tả ở đây chỉ là **định hướng** — vẫn tự dựng HTML/CSS/GSAP mới cho từng act, verify bằng
  Studio thumbnail + render thật.
