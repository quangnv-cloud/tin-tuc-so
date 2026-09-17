# COMPLIANCE — fed-tang-lai-suat-lan-dau-tien-sau-3-nam
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-17T07:03:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "fed tăng lãi suất" — vị trí #85/161 trong danh sách Google Trends VN (0-index 84), trafficApprox "200+", cũng xuất hiện dày trên category=news (≥7 bài VnExpress/Dân Trí/Tuổi Trẻ cùng sáng 17/9)
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image báo Tuổi Trẻ (?image=a96b798ba5ec), ảnh báo chí thời sự thật, không AI tái dựng; nhạc nền Lyria tự sinh (calm ambient, không lời, negative-prompt vocals); SFX từ bộ repo dùng chung; font Montserrat self-host; logo kênh"
claims_verified:
  - "Fed tăng lãi suất thêm 0,25 điểm phần trăm, lên 3,75-4%, ngày 16/9 — ?article=a96b798ba5ec (Tuổi Trẻ)"
  - "Lần đầu tiên kể từ năm 2023 — ?article=a96b798ba5ec"
  - "Chủ tịch Fed Kevin Warsh: lạm phát Mỹ 'quá cao trong thời gian quá dài' — ?article=a96b798ba5ec"
  - "Ủy ban Thị trường Mở Liên bang (FOMC) nhất trí thông qua — ?article=a96b798ba5ec"
  - "CPI Mỹ tháng 8 ở mức 3,4% — ?article=a96b798ba5ec"
  - "Mục tiêu lạm phát dài hạn của Fed 2% — ?article=a96b798ba5ec"
  - "PCE dự báo cuối năm nâng lên 3,7% — ?article=a96b798ba5ec"
  - "Tăng trưởng GDP dự báo nâng lên 2,3% — ?article=a96b798ba5ec"
  - "Ít nhất 12/18 nhà hoạch định chính sách dự báo cần thêm 1 đợt tăng lãi suất nữa trước cuối năm — ?article=a96b798ba5ec (nêu rõ là dự báo, không phải khẳng định chắc chắn)"
  - "Tổng thống Trump phản ứng giận dữ, gọi đây là 'đợt tăng lãi suất chống Trump' — ?article=a96b798ba5ec (trích dẫn trực tiếp từ báo)"
  - "Tỷ giá trung tâm 17/9 lên 25.632 đồng/USD, +6 đồng, cao nhất từ trước đến nay — ?article=f592159d5c19 (VnExpress Kinh doanh)"
  - "Giá vàng miếng SJC giảm 700.000 đồng/lượng, còn 142,8–145,8 triệu đồng/lượng — ?article=6c3b46f56032 (Dân Trí)"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Đã gỡ 1 con số suy luận số học ('mức lãi suất trước đó 3,5-3,75%') khỏi SCRIPT.md ở bước GATE B vì không có nguyên văn trong nguồn đã đối chiếu — thay bằng so sánh với mục tiêu 2% + CPI 3,4% (đều có nguyên văn nguồn). Minh bạch quy trình: 1 lệnh POST thăm dò cú pháp gọi nhầm với slug giả 'test-probe-ignore' đã vô tình tiêu tốn 1 lượt xoay vòng construction-style thật (Apps Script trả index:9 '10-stock-terminal' cho video giả đó) trước khi claim_style thật cho video này chạy (trả index:0 '1-card-and-bar', đã dùng đúng). Không ảnh hưởng nội dung/chất lượng video này."
