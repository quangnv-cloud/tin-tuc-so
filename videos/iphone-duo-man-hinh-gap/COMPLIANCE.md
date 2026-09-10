# COMPLIANCE — iphone-duo-man-hinh-gap

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-10T05:52:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "iphone duo (Google Trends VN, vị trí #27/187 theo mới nhất, trafficApprox 2000+; cùng cụm với 'apple event' #35/1000+, 'ios 27' #0/100+)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress (id 13e741a9db5e), có dẫn nguồn trong Hook + Article Image Card, không watermark ngoài logo báo gốc; nhạc nền sinh bằng Google Lyria (lyria-recipe.py, recipe calm, density 0.25/brightness 0.4, negative-prompt loại vocal), tự sinh riêng cho dự án này; SFX từ bộ palette dùng chung của kênh (impact-bass-1/whoosh-short/pop/chime/click-soft)"
claims_verified:
  - "Sự kiện 'Surprise and Shine', 0h ngày 10/9/2026 giờ Hà Nội (9/9 giờ Mỹ), tại Apple Park, kéo dài khoảng 80 phút — VnExpress (?article=13e741a9db5e)"
  - "Lần đầu lễ ra mắt iPhone do John Ternus dẫn dắt trong vai trò giám đốc điều hành Apple, sau khi tiếp quản từ Tim Cook — VnExpress"
  - "iPhone Duo — điện thoại màn hình gập đầu tiên của Apple, cũng là iPhone mỏng nhất từ trước đến nay — VnExpress + Dân Trí (?article=30fe26bb6495)"
  - "Màn hình mở ra 7,6 inch Super Retina XDR, màn hình ngoài 5,4 inch, ProMotion 120Hz, độ sáng tối đa 3.000 nit — VnExpress + Dân Trí (đối chiếu 2 nguồn, KHÔNG dùng con số % so sánh kích thước màn hình do 2 nguồn nêu 2 mốc so sánh khác nhau)"
  - "Khung titan, kính gia cường chống trầy màn hình trong — Dân Trí"
  - "Chip Apple A20 Pro dùng chung cho 18 Pro và Duo; băng thông bộ nhớ +50%, hiệu năng đồ hoạ (GPU 7 nhân) +40% so với thế hệ trước — VnExpress; tản nhiệt buồng hơi trên Duo giúp hiệu năng cao hơn 35% so với iPhone 17 Pro — VnExpress"
  - "Giá quốc tế: từ 1.999 USD (256GB) — VnExpress + Dân Trí"
  - "Giá Việt Nam: 65 triệu (256GB) / 71,5 triệu (512GB) / 84,5 triệu (1TB) / 104 triệu đồng (2TB) — Dân Trí"
  - "Đặt trước từ 16/10, bán ra 23/10 (quốc tế lẫn Việt Nam) — VnExpress + Dân Trí"
  - "iPhone 18 Pro/Pro Max thêm màu đỏ đậm, giá +100 USD so với thế hệ trước, đặt hàng 12/9, bán ra 18/9 — VnExpress"
  - "Trước iPhone Duo, thị trường điện thoại gập do Samsung dẫn dắt suốt gần một thập kỷ — tiêu đề bài VnExpress liên quan, dùng làm câu context, không suy đoán tương lai"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Video thứ 2 của kênh Tin Tức Số về sự kiện Apple 9/9-10/9/2026, nhưng khác hẳn video trước (iphone-18-ra-mat-viet-nam, khung sáng 9/9): video trước dựng từ tin đồn/dự đoán TRƯỚC sự kiện, video này dựng SAU sự kiện với số liệu đã xác nhận chính thức, tập trung vào sản phẩm mới hoàn toàn (iPhone Duo — điện thoại gập đầu tiên) chưa từng đưa tin, và dùng style dựng khác (6-ring-progress, index 5, thay vì 2-chip-and-leaderboard). Tổng thời lượng thiết kế 65.41s / render thật 65.43s. ElevenLabs quota hết ở lần chạy đầu (29 credit còn lại, cần 80/dòng) — user đã nạp thêm, sinh lại toàn bộ 7 dòng thành công lần 2, tổng voice 62.6s (đã rút ngắn kịch bản so với bản nháp đầu 75.4s để né trần 75s). Vòng 1 render: phát hiện act 2/3/4/5/6 (What/Facts/Data/Context/Impact) để trống đen quá nhiều ở nửa dưới khung (lỗi tái phát đã ghi trong BRAND-SYSTEM.md) — đã sửa: đôn nội dung/vòng radial xuống, phóng to ring ở act Data (620→700px) và Context (260→320px), đẩy caption/foot xuống gần mốc top:1650-1700, tỉ lệ margin đáy khớp với Hook/CTA tham chiếu; render lại vòng 2 xác nhận đã khắc phục qua so sánh frame. Verify 4 bước: (1) ffprobe 65.433333s; (2) silencedetect -35dB/0.6s — không phát hiện khoảng lặng chết; (3) trích frame tại 3.5/12/20.5/28.5/39/50.5/60s, xem bằng Read — đúng thiết kế, không phần tử bịa, cân bằng dọc đạt; (4) transcript Gemini gemini-flash-lite-latest (gemini-flash-latest bị 429 hết quota free-tier ngày, chuyển sang lite) — khớp SCRIPT.md 7/7 dòng, chỉ 1 lỗi nhận dạng âm gần giống ở dòng 1 ('Surprise and Shine' / 'rạng sáng' nghe thành 'Surprise and Shy' / 'dạng sáng' — lỗi ASR với cụm tiếng Anh xen tiếng Việt, không phải lỗi đọc lắp/viết tắt của giọng)."
```
