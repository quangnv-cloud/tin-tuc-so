# COMPLIANCE — bong-da-nu-viet-nam-vao-tu-ket-asiad-20

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-22T01:05:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "ket qua" (Google Trends VN, category=trend id 698bafcfa9d6) — vị trí #12/89 trong danh sách, trafficApprox 5000+; related khớp đúng chủ đề (Việt Nam - Thái Lan, tứ kết Asiad 20). Nhóm A2 — kết quả thể thao có yếu tố VN.
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress Thể thao (id 96ddd40398b3, ?image= endpoint), có dẫn nguồn, không watermark; nhạc nền Lyria tự sinh (calm ambient, density 0.25 brightness 0.4, negative-prompt vocals); SFX từ bộ repo (chime/click-soft/impact-bass/pop/whoosh-short)"
claims_verified:
  - "Hoà 0-0 trước Thái Lan, sân Nagai (Osaka), chiều 21/9/2026 — đối chiếu VnExpress Thể thao (id 96ddd40398b3) + Dân Trí (id 1350b2cd8165)"
  - "Việt Nam xếp thứ 3 bảng E, 1 điểm, hiệu số -9, đi tiếp nhờ là 1 trong 2 đội thứ ba có thành tích tốt nhất, vượt qua Myanmar (1 điểm, hiệu số -13) — theo ?article= VnExpress"
  - "Cầm bóng: Việt Nam 51% - Thái Lan 49%; dứt điểm: Việt Nam 3 - Thái Lan 8; dứt điểm trúng đích: 2-2 — theo ?article= Dân Trí"
  - "Thủ môn Kim Thanh cứu thua phút 51 (pha cản phá tình huống suýt phản lưới của Thanh Nhã) — theo ?article= VnExpress"
  - "Tứ kết ngày 25/9, đối thủ Trung Quốc — theo ?article= cả VnExpress và Dân Trí"
  - "Huấn luyện viên Hoàng Văn Phúc — theo tiêu đề bài Dân Trí"
sensitive_flags: []
vietnam_legal_flags: []
notes: |
  Chủ đề chọn qua category=trend ("ket qua"), đối chiếu category=news (id 96ddd40398b3 VnExpress +
  id 1350b2cd8165 Dân Trí) — 2 nguồn khớp nhau về tỷ số, địa điểm, ngày giờ, thống kê trận đấu.
  Không có claim nào tự nghĩ ra ngoài 2 bài báo trên. Style dựng: 10-stock-terminal (index 9, claim_style).
  Verify kỹ thuật: ffprobe duration 53.6s (dưới 75s); silencedetect sạch (không khoảng lặng chết);
  loudnorm 2-pass đưa về -14.4 LUFS / -1.5 dBTP (trong ngưỡng); transcript Gemini flash-latest khớp
  100% SCRIPT.md (không câu nào "chế thêm"); cân bằng dọc đã đo bằng pixel-diff cho cả 7 frame,
  phần tử cuối mỗi act giữa nằm trong khoảng top 1449-1621px (CTA/signature ở ~1717px theo đúng mẫu
  chữ ký logo cố định của các video trước); thumbnail (t=3.5s) hiển thị đủ logo, tên kênh, badge nguồn,
  tiêu đề, 2 tag tương phản, không mờ/cắt.
