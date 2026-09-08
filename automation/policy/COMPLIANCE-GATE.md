# COMPLIANCE GATE — cổng kiểm duyệt bắt buộc trước khi xuất bản

Rút gọn 2 policy engine (`youtube-google-policy-engine.md` + `meta-policy-engine.md`) thành
**checklist thao tác** cho routine tự động dựng video tin nóng / trending trong ngày (tiếng Việt,
kênh "Tin Tức Số") → đăng **Facebook Reel + YouTube Shorts**. Routine PHẢI chạy cổng này;
RED/ORANGE/BLACK → **DỪNG, không đăng**.

> **Tuyến "Tin Tức Số" bám Google Trends VN → GATE A ở đây SIẾT CHẶT hơn các tuyến khác.** Trends
> hằng ngày phần lớn là drama sao / thể thao nước ngoài / bê bối — đó chính là loại tin GATE A loại.
> Chấp nhận việc nhiều suất phải BỎ (skip) vì không có chủ đề an toàn — thà bỏ suất còn hơn hạ chuẩn.

Đọc bản đầy đủ khi gặp trường hợp không chắc — 2 file cùng thư mục này.

## Nguyên tắc nền

- 4 quyết định TÁCH RIÊNG: `post_allowed` · `recommendation` · `monetization` · `advertising`.
  Routine chỉ tự quyết `post_allowed` + đánh giá rủi ro monetization; không tự khẳng định "chắc chắn bật kiếm tiền".
- KHÔNG bịa: nguồn, số liệu, trích dẫn, screenshot, "case study", quy định pháp luật, chính sách nền tảng.
- KHÔNG hard-code ngưỡng chính sách cũ — với tin nhạy cảm phải nêu "cần kiểm tra nguồn chính thức".
- Mục tiêu KHÔNG phải "né nền tảng" mà là nội dung **nguyên bản, chính xác, hữu ích, minh bạch, bền vững cấp kênh**.

## GATE A — sàng lọc lúc CHỌN CHỦ ĐỀ (chạy ngay sau bước phát hiện trending + chọn tin, trước khi tốn công dựng)

Một chủ đề chỉ QUA GATE A khi vừa (a) đang trending / là tin nóng trong ngày, vừa (b) KHÔNG rơi vào
bảng loại dưới đây VÀ (c) có thể trình bày trung lập, xây dựng, không gây hại.

### A1 — BỎ NGAY (chọn chủ đề khác; nếu không còn chủ đề an toàn nào → BỎ SUẤT, ghi log)

| Loại | Mã | Ghi chú |
|---|---|---|
| Đời tư / drama / tin đồn / phát ngôn gây tranh cãi của người nổi tiếng, KOL, nghệ sĩ, streamer | ORANGE | Đây là phần LỚN NHẤT của Google Trends VN hằng ngày — mặc định loại hết. Chỉ giữ khi là **sự kiện nghề nghiệp trung lập** (ra album/phim, giải thưởng chính thức, lịch diễn) và không dính scandal. |
| Cáo buộc hình sự / khởi tố / bắt giữ / điều tra / kết án một cá nhân | ORANGE | Kể cả khi báo chính thống đã đưa. Routine không đủ năng lực verify + rủi ro bôi nhọ. |
| Tai nạn / án mạng / thảm kịch có nạn nhân cá nhân, đưa kiểu khai thác chi tiết | ORANGE | Thiên tai / tai nạn diện rộng đưa TRUNG LẬP mức cảnh báo cộng đồng thì xem A2. |
| Chính trị / bầu cử / nhân sự cấp cao / đối ngoại / chủ quyền / xung đột vũ trang | ORANGE / HUMAN REVIEW | Không đụng, kể cả tin "tích cực". |
| Thể thao nước ngoài thuần giải trí (giải ngoại hạng, tennis quốc tế, bóng đá châu Âu…) khi không có yếu tố VN | YELLOW→BỎ | Trending vì cá cược / fan quốc tế, không phải giá trị tin cho khán giả VN. Có vận động viên / đội tuyển VN tham gia → xem A2. |
| Y tế: "thuốc thần", cam kết chữa khỏi, khuyên bỏ điều trị, chống vắc-xin | RED | |
| Tài chính / tiền số: cam kết lợi nhuận, "insider", pump-and-dump, kèo, "x lần tài khoản" | RED | Tin kinh tế vĩ mô / chính sách / doanh nghiệp trung lập thì xem A2. |
| Deepfake / phát ngôn giả của người thật là NỘI DUNG CHÍNH | ORANGE | Chỉ tường thuật hiện tượng trung lập, KHÔNG tái dựng; không được thì bỏ. |
| Nội dung 18+, cờ bạc, chất kích thích, thử thách nguy hiểm | RED | |
| Khai thác trẻ em, bạo lực nghiêm trọng/đồ hoạ, lừa đảo, phishing, thù ghét | BLACK | Không bao giờ dựng. |
| Thuyết âm mưu, tin giả đã bị bác, "bí ẩn chưa lời giải" giật gân | RED | |
| Chủ đề chỉ có 1 nguồn thứ cấp / nguồn không rõ cho 1 claim lớn | — | Bỏ hoặc chờ nguồn tốt hơn. |

### A2 — ƯU TIÊN DỰNG (trending + an toàn) → **GREEN**

- Ra mắt / cập nhật sản phẩm, dịch vụ, công nghệ, ứng dụng, xe, thiết bị.
- Kết quả thể thao **có yếu tố VN** (đội tuyển VN, VĐV VN, giải trong nước) — tường thuật kết quả, số liệu.
- Chính sách / quy định mới đã ban hành (giao thông, giáo dục, thuế, lương, BHXH, giá điện/xăng…) — nêu **nội dung quy định**, không bình luận chính trị.
- Tin đời sống tích cực: thành tích học sinh/sinh viên VN, sáng chế, dự án cộng đồng, kỷ lục, du lịch, ẩm thực.
- Khoa học / vũ trụ / môi trường / thiên nhiên — phát hiện, sự kiện thiên văn, số liệu.
- Kinh tế trung lập: số liệu tăng trưởng, doanh nghiệp mở rộng/đầu tư, thị trường lao động (KHÔNG khuyến nghị đầu tư).
- Thời tiết / thiên tai / cảnh báo cộng đồng — đưa **mức thông tin & khuyến cáo an toàn**, dẫn nguồn cơ quan chức năng, KHÔNG khai thác đau thương, KHÔNG con số thương vong giật tít.
- Sự kiện văn hoá / giải trí trung lập: lịch chiếu phim, lễ hội, chương trình, giải thưởng chính thức.

### A3 — DỰNG ĐƯỢC nhưng GATE B siết (framing trung lập, "cáo buộc" ≠ "sự thật", nêu cần theo dõi nguồn chính thức) → **YELLOW**

- Tranh luận chính sách công nghệ (AI & việc làm, quyền riêng tư, bản quyền AI, quản lý mạng xã hội).
- Thu hồi sản phẩm / sự cố an toàn của một hãng — nêu khuyến cáo, dẫn thông báo chính thức.
- Vấn đề tiêu dùng / môi trường có bên bị nêu tên — phê bình **hành vi/sản phẩm/chính sách**, không phải cá nhân.

**Nếu không có chủ đề nào đạt A2/A3 trong khung giờ này → BỎ SUẤT**: ghi vào tóm tắt "skip slot — không có chủ đề trending an toàn", KHÔNG hạ chuẩn để lấp suất.

## GATE B — kiểm duyệt NỘI DUNG (chạy sau khi có SCRIPT.md + CAPTION.md + ảnh, trước render)

**B1. Sự thật & nguồn**
- [ ] Mọi số liệu / mốc thời gian / tên riêng / phát ngôn trong SCRIPT + CAPTION đều truy được về
  `?article=` (bài gốc) hoặc BRIEF. KHÔNG có con số nào routine tự nghĩ ra.
- [ ] Phân biệt rõ **cáo buộc / tin đồn / dự đoán** vs **sự thật đã xác nhận**. Dùng "được cho là",
  "theo …", "chưa được xác nhận" khi cần.
- [ ] Tin `intl` dịch lại: giữ đúng nghĩa bài gốc, KHÔNG thêm diễn giải/kết luận không có trong nguồn.
- [ ] Nếu tin có claim đang tranh cãi / chính sách nền tảng / pháp lý → thêm 1 câu "cần theo dõi
  thông báo/nguồn chính thức", KHÔNG chốt như sự thật tuyệt đối.

**B2. An toàn cộng đồng**
- [ ] Không kêu gọi / đe dọa / hướng dẫn bạo lực, tự hại, hành vi nguy hiểm actionable.
- [ ] Không công kích / phi nhân hóa / kích động thù ghét theo đặc điểm được bảo vệ. Phê bình
  **hành vi / sản phẩm / chính sách**, không phải con người.
- [ ] Không quấy rối, bôi nhọ, doxxing, lộ thông tin cá nhân không cần thiết.
- [ ] Không nội dung tình dục / khiêu dâm / liên quan trẻ em.

**B3. Chính hãng & liêm chính**
- [ ] KHÔNG giả danh: nền tảng (YouTube/Meta), ngân hàng, cơ quan nhà nước, hãng công nghệ,
  người nổi tiếng, chuyên gia. Kênh "Tin Tức Số" là kênh tin độc lập, KHÔNG mạo nhận là nguồn
  chính thức của hãng nào.
- [ ] Không testimonial giả, doanh thu giả, dashboard giả, "khách hàng của tôi kiếm X".
- [ ] Không engagement bait ("comment YES để lên xu hướng"). CTA phải là câu hỏi quan điểm thật.
- [ ] Không lừa đảo, phishing, fake giveaway, link độc hại trong caption/description.

**B4. AI / synthetic media (QUAN TRỌNG với tuyến này)**
- Giọng đọc: AI narrator chung (ElevenLabs "Khánh Lâm") = **GREEN**, KHÔNG cần disclosure
  (không giả giọng người thật cụ thể).
- Ảnh Hook / minh hoạ:
  - Ảnh thật lấy từ bài báo (`?image=`) trong Article Image Card có ghi nguồn = **GREEN** (dùng
    tin tức có dẫn nguồn). KHÔNG chỉnh sửa ảnh để bịa nội dung.
  - Ảnh do AI tạo kiểu **minh hoạ ý niệm / hoạt hoạ / cảnh hư cấu** (robot, sơ đồ, biểu tượng)
    = **GREEN**, KHÔNG cần disclosure.
  - ❌ TUYỆT ĐỐI KHÔNG dùng AI để: tái dựng **cảnh thật / người thật một cách như-ảnh-chụp**,
    tạo "hiện trường" giả, phát ngôn giả, ảnh bằng chứng giả, footage tin tức giả. Nếu 1 tin cần
    hình ảnh một sự kiện thật mà không có ảnh thật → dùng minh hoạ ý niệm rõ ràng là đồ hoạ, KHÔNG
    render ảnh giả như thật.
  - Nếu (ngoại lệ) có cảnh AI tả người/sự kiện thật ở mức dễ nhầm là thật → PHẢI thêm dòng chữ
    trên hình + trong description: **"Hình ảnh minh hoạ do AI tạo."** và khai AI content trong
    YouTube Studio. Mặc định tuyến này tránh trường hợp này.

**B5. Bản quyền & nhạc**
- [ ] Ảnh: chỉ dùng `?image=` (og:image bài báo, có dẫn nguồn) hoặc ảnh AI tự tạo / stock có quyền.
  KHÔNG lấy ảnh có watermark rồi cắt/xoá.
- [ ] Nhạc nền: Lyria tự sinh (không lời) = quyền của dự án. KHÔNG lấy nhạc từ video khác.
- [ ] SFX: bộ SFX trong repo. KHÔNG cố né Content ID (đổi tốc độ/pitch/mirror).
- [ ] Video KHÔNG phải reup / cắt ghép video của kênh khác — 100% tự dựng.

**B6. Tiêu đề & thumbnail (title/caption/description)**
- [ ] Tiêu đề = `sự kiện / số liệu chính` + góc tò mò hợp lý. KHÔNG "SỐC!!!", "100% CHẮC CHẮN",
  "YouTube xoá kênh ngày mai" khi không có bằng chứng.
- [ ] Thumbnail (frame Hook) phản ánh đúng nội dung, không gây hiểu sai, không giật gân quá mức,
  không hình ảnh bịa.
- [ ] Caption/description: giải thích nội dung + `📌 Nguồn` + hashtag liên quan. KHÔNG nhồi hashtag,
  KHÔNG hashtag không liên quan, KHÔNG từ khoá ẩn gây hiểu nhầm.

**B7. Nguyên bản (chống "inauthentic / mass-produced")** — rủi ro cao nhất với kênh tự động
- [ ] Video này có **ít nhất 1**: góc nhìn riêng / phân tích riêng / cách trình bày dữ liệu riêng /
  tổng hợp hữu ích. KHÔNG chỉ đọc lại tiêu đề báo.
- [ ] KHÔNG trùng bố cục/kịch bản với video gần nhất (đã có cơ chế `claim_style` xoay 10 style +
  quy tắc "mỗi video một cách dựng").
- [ ] Act 7 CTA đặt câu hỏi tranh luận THẬT bám tin, không phải bait chung chung.
- Ghi nhận: kênh đăng 3 video/ngày → phải giữ mỗi video có giá trị riêng, nếu 1 ngày không có tin
  đủ chất → thà bỏ 1 suất còn hơn đăng video rỗng (báo trong tóm tắt).

**B8. Pháp lý Việt Nam** — flag (ghi vào COMPLIANCE.md, KHÔNG tự dựng nếu dính) khi tin chạm:
an ninh mạng / an ninh quốc gia / trật tự công cộng / thông tin sai sự thật / bôi nhọ / dữ liệu
cá nhân / quảng cáo có điều kiện (tài chính, y tế, hàng kiểm soát) / sở hữu trí tuệ. KHÔNG tự bịa
số điều luật.

## GATE C — kiểm tra CUỐI (sau render + thumbnail, trước bước đăng)

- [ ] Xem lại thumbnail + 3-4 frame render: đúng B6, không có phần tử bịa, không lộ lỗi.
- [ ] Transcript (bước verify) khớp SCRIPT — không có câu nào routine "chế thêm" khi sinh voice.
- [ ] Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.

## OUTPUT — ghi `videos/<slug>/COMPLIANCE.md`

```
# COMPLIANCE — <slug>
policy_version: youtube v1.0 / meta v3.0
checked_at: <ISO>
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN | YELLOW | (nếu ORANGE/RED → đã bỏ chủ đề, không tới đây)
trending_signal: "<từ khoá Google Trends / vị trí trong list / approx_traffic>"  # rỗng nếu chọn từ category=news
GATE B (content):   GREEN | YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN | YELLOW
ai_disclosure_required: false        # true nếu B4 ngoại lệ
copyright_notes: "ảnh og:image <nguồn>, có dẫn nguồn; nhạc Lyria tự sinh"
claims_verified: [<liệt kê số liệu/mốc + đã đối chiếu ?article=>]
sensitive_flags: []                  # vd ["AI & việc làm — framing trung lập"]
vietnam_legal_flags: []
notes: ""
```

Nếu **decision != APPROVE** hoặc **risk_level in [ORANGE, RED, BLACK]** → **DỪNG routine ở đây**,
KHÔNG đăng Facebook/YouTube, ghi lý do rõ ràng vào tóm tắt cuối (giống tinh thần "bước sản xuất
thất bại → dừng").

## Bảng quyết nhanh (tuyến tin nóng / trending — "Tin Tức Số")

| Tình huống | Kết quả |
|---|---|
| Ra mắt sản phẩm/dịch vụ/công nghệ; chính sách mới đã ban hành; khoa học; kết quả thể thao có yếu tố VN; tin đời sống tích cực | GREEN → APPROVE |
| Trending vì drama / tin đồn / phát ngôn gây tranh cãi của người nổi tiếng | ORANGE → BỎ CHỦ ĐỀ ở GATE A |
| Trending vì cáo buộc hình sự / khởi tố / bắt giữ một cá nhân | ORANGE → BỎ CHỦ ĐỀ ở GATE A |
| Chính trị / bầu cử / nhân sự cấp cao / đối ngoại / chủ quyền | ORANGE/HUMAN REVIEW → BỎ CHỦ ĐỀ ở GATE A |
| Thể thao nước ngoài thuần giải trí, không yếu tố VN | YELLOW→BỎ ở GATE A |
| Thiên tai / thời tiết / cảnh báo cộng đồng | GREEN nếu đưa mức thông tin + khuyến cáo an toàn, dẫn nguồn cơ quan chức năng, KHÔNG khai thác thương vong |
| Thu hồi sản phẩm / sự cố an toàn của một hãng | YELLOW → nêu khuyến cáo + thông báo chính thức → APPROVE |
| Tranh luận chính sách công nghệ (AI & việc làm, quyền riêng tư, bản quyền AI) | YELLOW → framing trung lập, nêu cần theo dõi nguồn chính thức → APPROVE |
| Ảnh AI minh hoạ ý niệm (bản đồ, sơ đồ, biểu tượng) | GREEN, không cần disclosure |
| Ảnh AI tả người thật/sự kiện thật như ảnh chụp | RED → đổi sang minh hoạ ý niệm, hoặc bỏ chủ đề |
| Số liệu không có trong bài gốc | RED → sửa/bỏ dòng đó, sinh lại voice |
| Tiêu đề giật gân quá bằng chứng | YELLOW → viết lại `sự kiện + tò mò hợp lý` |
| Y tế "thuốc thần" / tài chính "cam kết lãi" / tiền số "kèo" / 18+ / cờ bạc | RED → BỎ CHỦ ĐỀ ở GATE A |
| Deepfake/phát ngôn giả là nội dung chính | ORANGE → chỉ tường thuật trung lập, không tái dựng; nếu không được thì bỏ |
| Lừa đảo / phishing / khai thác trẻ em / bạo lực nghiêm trọng / thù ghét | BLACK → không bao giờ dựng |
| Cả khung giờ không có chủ đề trending nào đạt A2/A3 | BỎ SUẤT — ghi "skip slot" vào tóm tắt, KHÔNG hạ chuẩn |
