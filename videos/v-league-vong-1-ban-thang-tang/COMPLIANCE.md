# COMPLIANCE — v-league-vong-1-ban-thang-tang

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-09T07:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "giải bóng đá vô địch quốc gia việt nam (Google Trends VN, vị trí #74/112 theo mới nhất, trafficApprox 200+)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh minh hoạ (Hook + Article Image Card, act 'Chuyện gì xảy ra') là og:image thật lấy qua endpoint ?image= của báo Tuổi Trẻ (id bad08b6d7743, bài 'CLB Becamex TP.HCM xuất quân, quyết trở lại V-League', 1200x750px, ảnh chụp thật một pha bóng V-League có logo giải VPF trên biển quảng cáo sân) — dùng làm ảnh minh hoạ KHÔNG khí V-League nói chung, chú thích trên video chỉ ghi 'Mùa giải 2026-2027' (không gắn tên trận đấu/cầu thủ cụ thể nào trong SCRIPT, tránh gây hiểu sai theo B6). Nội dung/số liệu và badge 'Nguồn' trên toàn video ghi nguồn nội dung chính là Báo Thanh Niên (qua ?article=d3353fbbf7ab). Nhạc nền do Google Lyria tự sinh (instrumental, không lời, negative-prompt loại vocal). SFX (chime/click-soft/impact-bass-1/pop/whoosh-short) lấy từ videos/_reference-astra-openai/assets/sfx/ (kho SFX nội bộ repo, đã dùng ở video trước cùng kênh). Không sử dụng ảnh có watermark, không tái dựng cảnh/người thật bằng AI."
claims_verified:
  - "Vòng 1 giải bóng đá vô địch quốc gia Việt Nam mùa 2026-2027: 7 trận, tổng 23 bàn thắng — đối chiếu BRIEF.md / ?article=d3353fbbf7ab (Báo Thanh Niên)"
  - "Nhiều hơn 3 bàn so với vòng mở màn mùa trước (tức mùa trước vòng 1 có 20 bàn) — đối chiếu BRIEF.md, nguyên văn báo Thanh Niên"
  - "Trung bình hơn 3 bàn/trận, 'một con số ấn tượng cho vòng đấu đầu tiên' — nguyên văn báo Thanh Niên, đối chiếu BRIEF.md"
  - "Nam Định thắng Hoàng Anh Gia Lai 4-0 — đối chiếu BRIEF.md"
  - "Ninh Bình thắng Hải Phòng 4-1 — đối chiếu BRIEF.md"
  - "Thanh Hóa thắng Đà Nẵng 3-2 — đối chiếu BRIEF.md"
  - "Cầu thủ nội nổi bật: Tiến Linh, Xuân Son, Đình Bắc (và Williams Minh Hoàng, Quang Vinh, Đoàn Văn Hậu, Patrik Lê Giang trong BRIEF, không đưa hết vào script/hình do giới hạn thời lượng) — đối chiếu BRIEF.md"
  - "Việt kiều trẻ tỏa sáng: Trần Thành Trung (Ninh Bình), Tran Lenn Minh Quang (Công an TP.HCM, hiển thị 'Minh Quang'), Tyler James Thai Crawford (Nam Định, hiển thị 'Tyler Crawford') — đối chiếu BRIEF.md, đúng theo báo"
  - "Tân binh nổi bật vòng 1: Ezequiel Santos (Nam Định), Saliou Guindo (Thanh Hóa), dàn tân binh Thể Công Viettel — đối chiếu BRIEF.md"
  - "Công tác trọng tài/VAR không có tình huống tranh cãi đáng kể xuyên suốt vòng 1 — đối chiếu BRIEF.md, nguyên văn báo Thanh Niên"
  - "HLV Kim Sang-sik đang tìm nhân tố mới cho đội tuyển Việt Nam, hướng tới giải bóng đá vô địch Đông Nam Á sắp tới — nêu là bối cảnh có thật (giải đấu sắp diễn ra), KHÔNG suy đoán kết quả tương lai của đội tuyển, đối chiếu BRIEF.md"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Nhóm A2 (kết quả thể thao có yếu tố VN, giải trong nước) — không đụng đời tư cầu thủ, không yếu tố hình sự/chính trị. Ảnh hero không phải ảnh của 3 trận đấu cụ thể được nêu trong script (do ?image= của item trending/news đúng chủ đề đều không dùng được — xem BRIEF.md mục Ảnh minh hoạ) — đã xử lý bằng caption trung lập 'Mùa giải 2026-2027' và không gắn tên đội/cầu thủ cạnh ảnh, giữ badge nguồn nội dung là Thanh Niên xuyên suốt (tiền lệ tương tự video iphone-18-ra-mat-viet-nam dùng ảnh Dân Trí trong khi badge nguồn là VnExpress). Voiceover giữ đúng SCRIPT.md đã chốt (không viết tắt V-League/VAR trong lời đọc); verify phiên âm ngược (Gemini gemini-flash-latest, transcribe từng dòng line1-7.mp3 riêng) khớp chính xác nội dung 7 dòng, không phát hiện lỗi đọc lắp/đánh vần/sai nghĩa."
```
