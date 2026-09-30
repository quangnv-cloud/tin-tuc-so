# COMPLIANCE — huyen-thoai-toan-hoc-viet-nam-le-ba-khanh-trinh

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-22T07:00:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "" — chọn từ `category=news` (Báo Dân Trí, id `3f59a76e4e65`), KHÔNG qua Google
  Trends. Lý do: toàn bộ `category=trend` tại thời điểm kiểm (22/9/2026 ~06:22 UTC, 91 item) đều
  rơi vào nhóm A1 — xổ số/cờ bạc (xsmb/xsmt/xsmn, trafficApprox 100.000+), bóng đá châu Âu thuần
  giải trí không yếu tố VN (Real Madrid, MU, Liverpool, Napoli, Juventus, Bundesliga...), đời tư/
  tang lễ nghệ sĩ ("lan hương như cố"), tin đồn cá nhân ("trương minh huy vũ con ai") — không có
  mục nào đạt A2/A3. Chuyển sang `category=news`, chọn bài feature giáo dục tích cực (nhóm A2 —
  "tin đời sống tích cực: thành tích học sinh/sinh viên Việt Nam").
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh do báo Dân Trí đăng kèm bài (?image=3f59a76e4e65), ảnh lưu niệm thật chụp
  năm 2013, có dẫn nguồn, không watermark; nhạc nền Lyria tự sinh (calm ambient, density 0.25
  brightness 0.4, negative-prompt vocals/lyrics/singing/choir/rap/spoken word/humming); SFX từ bộ
  repo (impact-bass/whoosh-short/pop/click-soft/chime); giọng đọc ElevenLabs 'Khánh Lâm' (AI
  narrator chung, không giả giọng người thật cụ thể)."
claims_verified:
  - "Bức ảnh chụp năm 2013: tiến sĩ Lê Bá Khánh Trình cùng 2 học trò Cấn Trần Thành Trung, Phạm
    Tuấn Huy, ngay sau khi cả hai giành Huy chương Vàng Olympic Toán học quốc tế — theo ?article=
    Dân Trí (id 3f59a76e4e65)."
  - "Thầy Lê Bá Khánh Trình: năm 1979, 17 tuổi, giải Nhất Olympic Toán học quốc tế tại London,
    điểm tuyệt đối 40/40, giải Đặc biệt duy nhất năm đó — theo ?article=."
  - "32 năm (1993–2025) làm tổ trưởng Tổ Toán Trường Phổ thông Năng khiếu; đội tuyển giành 171
    giải học sinh giỏi quốc gia, 19 huy chương Olympic quốc tế (5 Vàng, 9 Bạc, 3 Đồng, 2 bằng khen
    danh dự) — theo ?article=."
  - "Phạm Tuấn Huy: thêm 1 Huy chương Vàng năm 2014 (tổng 2 HCV); cử nhân Toán + thạc sĩ Thống kê
    tại Stanford, thạc sĩ nghiên cứu Toán tại Cambridge, bảo vệ tiến sĩ tại Stanford; hiện là
    nghiên cứu viên sau tiến sĩ Viện Toán học Clay (CMI, Mỹ) — theo ?article=."
  - "Cấn Trần Thành Trung: học bổng toàn phần Đại học Duke, tốt nghiệp thủ khoa ngành Toán 2018;
    tiến sĩ Toán học tại Viện Công nghệ California (Caltech); 2024 trúng tuyển chương trình VNU350
    của ĐHQG TPHCM; hiện giảng dạy tại Trường Đại học Khoa học Tự nhiên — theo ?article=."
sensitive_flags: []
vietnam_legal_flags: []
notes: |
  Chủ đề chọn qua category=news (Dân Trí, id 3f59a76e4e65) sau khi toàn bộ category=trend không có
  mục nào qua GATE A (chi tiết ở BRIEF.md và trending_signal phía trên). Không có claim nào tự
  nghĩ ra ngoài bài báo gốc; đã sửa 1 lỗi bản nháp trước khi dựng (gán nhầm Viện Công nghệ
  California cho Phạm Tuấn Huy thay vì Cấn Trần Thành Trung) — đối chiếu lại nguyên văn bài báo và
  sửa đúng trước khi viết SCRIPT.md.

  Style dựng: 1-card-and-bar (index 0, claim_style). Thẻ thông số bo góc cho thành tích 1979 của
  thầy Trình (act Key facts) + cột so sánh dọc count-up cho huy chương Vàng/Bạc/Đồng (act Data
  moment), bảng nhãn trái/giá trị phải cho hành trình 2 học trò (act Context), 2 thẻ lớn cạnh nhau
  cho vị trí hiện tại (act Impact) — đúng ẩn dụ CONSTRUCTION-STYLES.md, không trùng bố cục video
  gần nhất (bong-da-nu-viet-nam-vao-tu-ket-asiad-20 dùng style 10-stock-terminal).

  Verify kỹ thuật (5 bước):
  1) ffprobe duration 70.400000s (thiết kế 70.369796s, dưới ngưỡng 75s).
  2) silencedetect noise=-40dB:d=0.6 — sạch, không khoảng lặng chết giữa video.
  3) loudnorm: Input Integrated -14.1 LUFS / True Peak -1.2 dBTP (trong ngưỡng -14 LUFS ±1 LU và
     ≤ -1.0 dBTP) sau 2 lần hiệu chỉnh loudnorm 2-pass (bản gốc render ở -15.5 LUFS, lệch quá ±1 LU
     nên đã chạy loudnorm linear=true hiệu chỉnh 2 lần để vừa đạt LUFS vừa giữ true peak an toàn).
  4) Trích frame thật cuối animation-reveal của cả 7 act, xem bằng Read: Hook/CTA đúng mẫu cố định
     brand; 5 act giữa (What/Facts/Data/Context/Impact) phần tử cuối cùng nằm trong khoảng top
     ~1440–1520px (đã phát hiện 2 frame đầu tiên kết thúc sớm ở ~1338px/~1406px lúc kiểm lần đầu,
     đã sửa CSS margin-top/gap và render lại — xác nhận lại bằng frame thật, không còn trống đen
     nửa dưới khung).
  5) Transcript (ElevenLabs STT scribe_v1 trên track audio cuối cùng, sau khi Gemini flash-latest
     bị chặn bởi lỗi 429 quota) khớp 100% với SCRIPT.md, không câu nào "chế thêm" khi sinh voice
     (chỉ khác cách viết số: STT chuẩn hoá số đọc thành chữ số, ví dụ "1979" thay vì phiên âm từng
     chữ — không phải lỗi nội dung).

  Thumbnail (t=3.5s, trong cửa sổ ổn định sau animation Hook ~2.32s): logo + tên kênh + badge
  nguồn + tiêu đề "LÊ BÁ KHÁNH TRÌNH" + 2 tag tương phản ("Thầy huyền thoại" / "2 trò vô địch thế
  giới") đều hiển thị đầy đủ, rõ nét, không mờ/cắt.
