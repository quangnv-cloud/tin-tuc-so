# COMPLIANCE — cpi-my-thang-8-fed-tang-lai-suat

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-12T01:15:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "cpi mỹ" (Google Trends VN, id aefa3c383f79, vị trí #60/240 trong danh sách,
  trafficApprox "200+", pubDate 2026-09-11T12:50:00Z)
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card lấy từ ?image=02c4923b9045 (CDN báo Dân Trí, ảnh báo
  gốc có dẫn nguồn, chân dung Chủ tịch Fed Kevin Warsh tại sự kiện/điều trần công khai — nhân vật
  được nêu tên trực tiếp trong bài viết dùng làm nguồn văn bản chính, ảnh báo chí thời sự thông
  thường không dàn dựng, không chỉnh sửa nội dung, không watermark ngoài); nhạc nền sinh bằng Google
  Lyria (lyria-recipe.py, preset calm, density 0.25/brightness 0.4, negative-prompt loại bỏ giọng
  hát/lời), 100% không lời, thuộc quyền dự án, data-volume 0.30, carve --strength 0.4; SFX từ thư
  viện repo (_reference-astra-openai/assets/sfx); giọng đọc ElevenLabs 'Khánh Lâm - tin tức, thời
  sự' (voice_id RCmOaM1iiIH5xX3QXjIF, model eleven_v3, speed 1.09)."
claims_verified:
  - "CPI Mỹ tháng 8 tăng 0,4% so với tháng trước, tăng 3,4% so với cùng kỳ năm ngoái, đúng dự báo — Dân Trí (?article=aefa3c383f79, fetch related[0])"
  - "CPI lõi tăng 0,3% theo tháng, cao hơn dự báo 0,1 điểm phần trăm, lạm phát lõi cả năm 2,4% — Dân Trí"
  - "Xác suất Fed tăng thêm 0,25 điểm phần trăm lãi suất tuần tới vọt từ khoảng 70% lên gần 90% (FedWatch/CME Group, ghi nhận CNBC/WSJ) — Dân Trí"
  - "Giá xăng tăng 3,9% trong tháng, đóng góp hơn 1/3 mức tăng CPI chung — Dân Trí"
  - "Thị trường lao động Mỹ thêm 162.000 việc làm mới tháng 8, vượt dự báo — Dân Trí"
  - "Chứng khoán Mỹ sáng 11/9 tăng điểm nhờ giá dầu hạ nhiệt, Dow Jones tăng gần 600 điểm (~1%) — Dân Trí"
  - "Lợi suất trái phiếu chính phủ kỳ hạn 2 năm tăng lên 4,594% (làm tròn 'khoảng 4,6%' trong SCRIPT cho tự nhiên khi đọc) — Dân Trí"
  - "Lãi suất quỹ liên bang hiện ở biên độ 3,5-3,75%; cuộc họp chính sách Fed vào tuần tới — Dân Trí (chỉ nêu lịch họp + xác suất thị trường, KHÔNG khẳng định kết quả)"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chủ đề kinh tế vĩ mô Mỹ trung lập (A2), không đụng chính trị/đối ngoại VN. Có nêu tên một
  quan chức công (Chủ tịch Fed Kevin Warsh) trong vai trò điều hành chính sách công khai, dùng ảnh
  báo chí thời sự thật (không phải đời tư/drama cá nhân) — không rơi vào nhóm A1. KHÔNG đưa chi tiết
  'căng thẳng Trung Đông' (có trong bài gốc, ảnh hưởng giá dầu) vào SCRIPT/CAPTION để tránh chạm
  nhóm A1 'đối ngoại/xung đột vũ trang', theo đúng tiền lệ video giá xăng dầu trước đó — giữ trọng
  tâm 100% ở số liệu CPI/lãi suất Mỹ.

  [QA vòng render đầu] Agent dựng composition báo cáo đạt cân bằng dọc ở cả 7 act, nhưng khi tôi tự
  trích frame độc lập từ file .mp4 đã render (t=30s, act Data moment) phát hiện phần tử cuối cùng
  của frame chỉ dừng ở y≈710/1920 (37%) — vi phạm rõ ràng quy tắc 'Cân bằng dọc' của BRAND-SYSTEM.md
  (yêu cầu 1400-1680px), đồng thời act này thiếu hẳn bảng xếp hạng ngang (leaderboard trước/sau báo
  cáo) theo đúng định hướng style `2-chip-and-leaderboard` đã claim — chỉ có 1 số to + 1 đoạn văn.
  Gửi lại yêu cầu sửa: nguyên nhân là timing GSAP nội bộ của act để lộ trạng thái leaderboard quá
  muộn (chỉ hiện đủ sau ~4.1s trong khi mẫu lấy ở giữa act). Agent sửa lại mốc reveal nội bộ (không
  đổi data-duration/timing tổng), render lại, đo lại bằng ffprobe/silencedetect/frame/transcript từ
  đầu. Sau fix, tôi tự trích lại frame tại t=30s bằng ffmpeg độc lập và đo pixel chính xác bằng PIL
  (không chỉ xem bằng mắt) — xác nhận phần tử cuối (bảng xếp hạng trước ~70%/sau ~90% + dòng nguồn
  chú thích) nay dừng ở y=1455/1920 (75,8%), trong khoảng yêu cầu, và bảng xếp hạng 2 hàng theo đúng
  style đã hiện diện.

  [Một nghi vấn đã tự loại trừ] Ở frame CTA (act 7), lần xem bằng mắt qua ảnh preview nén khiến tôi
  nghi ngờ chữ ký logo bị cắt ngắn ở y≈1210 kèm khoảng đen lớn phía dưới — nhưng đo lại chính xác
  bằng phân tích pixel (PIL, quét từng dòng so màu nền) trên chính file render, ở nhiều mốc thời gian
  trong act (63s-74s), cho kết quả nhất quán: phần tử cuối (chữ ký logo, CSS `bottom:240px`) luôn ở
  y=1678/1920 (87,4%) — đúng trong khoảng 1400-1680px yêu cầu, khớp với CSS thiết kế. Kết luận: nghi
  vấn ban đầu là sai số khi nhìn ảnh preview bị nén/thu nhỏ (chữ ký nhỏ, màu trắng mờ 85% opacity
  trên nền gần đen, khó thấy ở kích thước hiển thị nhỏ) — KHÔNG phải lỗi thật, đã xác minh lại bằng
  phép đo định lượng trước khi kết luận, không sửa gì thêm ở frame này.

  Kết quả cuối: 7/7 frame đạt cân bằng dọc (đo pixel: Hook 1519/79%, What-happened ~1470,
  Key facts 1539/80%, Data moment 1455/76%, Context 1407/73%, Impact ~1425, CTA 1678/87%)."
```
