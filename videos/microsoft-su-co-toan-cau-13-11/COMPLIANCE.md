# COMPLIANCE — microsoft-su-co-toan-cau-13-11
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-11-13T14:20:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): YELLOW   # A3 — sự cố dịch vụ của một hãng công nghệ; tường thuật trung lập, nguyên nhân chỉ nêu theo thông báo của Microsoft
trending_signal: "microsoft sập — Google Trends VN, vị trí 59/233, approx_traffic 2000+ (kèm 'outlook bị sập' vị trí 58/233, 1000+); có ở category=news: VnExpress Khoa học ×2, Tuổi Trẻ"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress (Hook: điện thoại báo lỗi Outlook — ?image=dcb3c77eece5; Act 2: biển hiệu Microsoft — ?image=06b9bbe1f40a, ghi 'Ảnh: VnExpress'); ảnh minh hoạ ghép của Tuổi Trẻ cố ý KHÔNG dùng; nhạc nền Google Lyria tự sinh (không lời); giọng AI narrator chung (Vbee HN - Minh Quân, tài khoản GỐC); SFX trong repo; icon CSS tự vẽ, không dùng logo sản phẩm; video 100% tự dựng"
claims_verified:
  - "Sự cố bắt đầu khoảng 1h 13/11 giờ VN, quy mô toàn cầu; Microsoft 365, Outlook, Teams, Copilot, Store — VnExpress ?article=a9d4390b4c09, 06b9bbe1f40a; Tuổi Trẻ ?article=899e457ed95d"
  - "Kéo dài hơn nửa ngày (Guardian: bất thường) — VnExpress 06b9bbe1f40a"
  - "VN: không vào được email/Outlook, lịch họp, OneDrive/SharePoint chập chờn; Downdetector VN hơn 200 báo lỗi Outlook — VnExpress ?article=dcb3c77eece5"
  - "OpenAI kiểm tra lỗi trình kết nối Microsoft; Anthropic xác nhận lỗi nhà cung cấp thượng nguồn ảnh hưởng connector Microsoft 365 (theo Reuters) — VnExpress, Tuổi Trẻ"
  - "Downdetector Mỹ: ~130.000 Outlook, >45.000 Microsoft 365, >10.000 Store — VnExpress, Tuổi Trẻ (trùng khớp); biểu đồ cột vẽ đúng tỉ lệ 130/45/10"
  - "Không do lưu lượng tăng; nhiều máy chủ bất ngờ không hoạt động bình thường, gây áp lực lên phần còn lại; chưa có dấu hiệu tấn công mạng; nguyên nhân gốc chưa xác định chính thức — phát ngôn Microsoft qua VnExpress, Tuổi Trẻ"
  - "10h: thay đổi 'không đạt hiệu quả như kỳ vọng'; 16h: 'ổn định ban đầu' — VnExpress 06b9bbe1f40a"
  - "29/10 Azure sự cố toàn cầu hơn 8 giờ; Alaska Airlines, Heathrow, Vodafone — VnExpress a9d4390b4c09, Tuổi Trẻ"
  - "Workhorse Group lùi công bố KQKD quý III/2026 từ 12/11 sang 16/11 — VnExpress, Tuổi Trẻ"
  - "Một số cơ sở y tế ở Úc quay lại đơn thuốc giấy (AMA, theo Guardian) — VnExpress dcb3c77eece5"
sensitive_flags: ["Sự cố dịch vụ của hãng — nguyên nhân chỉ nêu theo thông báo chính thức, ghi rõ 'đang điều tra'", "Nhắc 'tấn công mạng' chỉ để dẫn phủ nhận của Microsoft, không suy đoán"]
vietnam_legal_flags: []
notes: "Suy đoán của các chuyên gia (lỗi cấu hình lớp mạng, so sánh Optus 2023) và suy đoán 'tấn công hạ tầng' trên mạng cố ý KHÔNG đưa vào. Voice dòng 2 sinh lại 1 lần (bản đầu 'mười ba tháng mười một' bị STT nghe thành 'tháng 10') → đổi thành 'ngày mười ba', ngày hiển thị trên hình. Transcript Gemini (gemini-3-flash-preview) khớp SCRIPT; Gemini tự thêm 'tháng 11' ở câu 2 nhưng ElevenLabs STT trên line2.mp3 xác nhận audio chỉ đọc 'ngày 13'. Loudness -14.5 LUFS, TP -1.0 dBTP (loudnorm 2-pass). Render lần 2 sau khi sửa cân bằng dọc Act 2/3 (Act 3 bản đầu dừng ở ~1166px). Act 6 chỉ nêu sự thật đã xảy ra; câu hỏi chỉ ở CTA."
