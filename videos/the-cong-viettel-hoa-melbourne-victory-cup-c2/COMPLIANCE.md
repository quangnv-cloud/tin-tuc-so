# COMPLIANCE — the-cong-viettel-hoa-melbourne-victory-cup-c2

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-17T01:05:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "thể công gặp melbourne victory — trafficApprox 10000+ (đỉnh danh sách Google Trends VN khung giờ này, 2 item cùng chủ đề id 57cf0e75bf04 / 4b453214b99f)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card = ảnh báo thật lấy qua ?image=11f07e3d785d (Báo Dân Trí, có dẫn nguồn, không chỉnh sửa nội dung); nhạc nền sinh bằng Google Lyria (recipe calm, instrumental, không lời — dự án tự sinh); SFX từ bộ có sẵn trong repo (videos/_reference-astra-openai/assets/sfx/); giọng đọc AI ElevenLabs 'Khánh Lâm' — giọng chung, không giả giọng người thật cụ thể."
claims_verified:
  - "Trận đấu: Thể Công Viettel (Việt Nam) – Melbourne Victory (Úc), lượt trận thứ nhất vòng bảng E, Cúp C2 châu Á (AFC Champions League Two) 2026-2027, sân Hàng Đẫy (Hà Nội), tối 16/9/2026 — đối chiếu Dân Trí + VietNamNet (related)."
  - "Kết quả: hòa 1-1 — khớp cả 2 nguồn (Dân Trí, VietNamNet)."
  - "Phút 46: bàn thắng của Lucas Ribamar (Thể Công Viettel) bị từ chối do lỗi chạm tay trước đó — theo Dân Trí."
  - "Phút 58: Clarismario (Melbourne Victory) ghi bàn vượt lên dẫn trước 1-0, qua mặt hậu vệ, sút qua thủ môn Văn Việt — theo Dân Trí."
  - "Phút 62: Phan Tuấn Tài tạt bóng, Lucas Ribamar đánh đầu gỡ hòa 1-1 (ấn định tỷ số chung cuộc) — theo Dân Trí."
  - "Thể Công Viettel tạm xếp thứ hai bảng E, sau Persib Bandung (Indonesia); Persib Bandung thắng FC Seoul (Hàn Quốc) 1-0 cùng ngày — theo Dân Trí."
  - "Bối cảnh: Thể Công Viettel thắng CLB Đồng Nai 2-0 ở trận mở màn V-League 2026-2027 — theo Dân Trí (không phải nội dung chính, chỉ dùng làm bối cảnh)."
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chủ đề thuộc nhóm A2 (kết quả thể thao có yếu tố VN — câu lạc bộ Việt Nam Thể Công Viettel thi đấu cúp châu lục). Đã lướt và loại các chủ đề trending khác cùng khung giờ: thể thao nước ngoài thuần giải trí không yếu tố VN (La Liga, Premier League, EFL Cup, Europa League, AFC Champions League Elite các đội không VN, U-23 các đội châu Á khác không VN) → A1 BỎ; chính trị (\"tô lâm\") → A1 BỎ NGAY; đời tư nghệ sĩ (\"trấn thành\", \"mạc văn khoa\", \"doãn quốc đam\", \"ninh dương lan ngọc\") → A1 BỎ; từ khoá quá chung chung không đủ dữ kiện (\"tiết kiệm\", \"phần mềm\", \"thuế\", \"chung cư\", \"nhiệm kỳ\") → BỎ. Style dựng: 7-timeline-chronology (index 6, claim_style), khớp tự nhiên với diễn biến trận đấu theo mốc phút. B7 (nguyên bản): góc trình bày riêng — trục thời gian trận đấu + tách biệt data moment (khoảnh khắc gỡ hòa) khỏi context (toàn bộ diễn biến) + impact (bảng xếp hạng), không chỉ đọc lại tiêu đề báo. Verify 5 bước: (1) ffprobe duration 61.0s (thiết kế 60.90s, chênh lệch do remux audio AAC — không đổi nội dung); (2) silencedetect noise=-40dB d=0.6 — không phát hiện khoảng lặng chết; (3) loudnorm — Integrated -14.7 LUFS (trong ±1 LU so với -14.0), True Peak -2.8 dBTP (dưới ngưỡng -1.0 dBTP) sau khi chạy loudnorm 2-pass (đo lần đầu -15.6 LUFS, lệch quá ±1 LU nên đã sửa); (4) trích 7 frame cuối animation-reveal của cả 7 act, đo bằng PIL (quét pixel khác nền #0B0E14) — tất cả nằm trong 1400-1680px (Hook 1467/76%, What 1563/81%, Facts 1506/78%, Data 1538/80%, Context 1599/83%, Impact 1439/75%, CTA 1577/82% — đã sửa CTA từ vị trí ban đầu 1747/91% do chữ ký logo đặt quá thấp, chạm vùng UI nền tảng 11-17% đáy khung); (5) transcript qua Gemini multimodal (gemini-flash-latest, Whisper bị chặn ở sandbox) khớp hoàn toàn SCRIPT.md, không có câu nào bị chế thêm hay bỏ sót. Phát hiện + sửa 1 lỗi kỹ thuật thật trong lần render đầu: caption karaoke giữa 2 chunk liền kề tạo hiệu ứng chữ chồng lên nhau khó đọc trong ~0.1-0.3s mỗi lần chuyển câu (xác nhận bằng ảnh trích thật, không phải chỉ cảnh báo lint) — đã sửa thuật toán chia thời điểm hiện/ẩn để chunk sau chỉ hiện sau khi chunk trước đã ẩn hoàn toàn, render lại, xác nhận đã sạch."
