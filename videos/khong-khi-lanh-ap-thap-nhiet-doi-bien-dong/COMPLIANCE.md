# COMPLIANCE — khong-khi-lanh-ap-thap-nhiet-doi-bien-dong

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-10T07:00:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "thời tiết áp thấp nhiệt đới (Google Trends VN, vị trí #17/196 theo mới nhất, trafficApprox 5000+; related trỏ thẳng bài Dân Trí dùng làm nguồn); đối chiếu category=news có ≥2 bài cùng chủ đề (Dân Trí + Tuổi Trẻ) số liệu trùng khớp"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Dân Trí (id e71179c125db, ảnh thật người dân TPHCM che mưa, có dẫn nguồn trong Hook + Article Image Card), không watermark ngoài nguồn gốc báo; nhạc nền sinh bằng Google Lyria (lyria-recipe.py, recipe calm, density 0.25/brightness 0.4, negative-prompt loại vocal), tự sinh riêng cho dự án này; SFX từ bộ palette dùng chung của kênh (impact-bass-1/whoosh-short/pop/chime/click-soft)"
claims_verified:
  - "Sáng/chiều 9/9, Trung tâm Dự báo khí tượng thuỷ văn quốc gia ghi nhận một vùng áp thấp hình thành trên dải hội tụ nhiệt đới giữa Biển Đông — Dân Trí (?article=e71179c125db) + Tuổi Trẻ (?article=c856322eaecf), số liệu khớp 2 nguồn"
  - "Trong 1-2 ngày tới, khả năng khoảng 80% mạnh lên áp thấp nhiệt đới; khả năng khoảng 30-40% mạnh lên thành bão — nếu thành sẽ là bão số 6 trong năm — Dân Trí + Tuổi Trẻ (khớp 2 nguồn)"
  - "Không khí lạnh đầu mùa đến sớm hơn trung bình nhiều năm khoảng 3-5 ngày (trung bình nhiều năm 12/9-4/10; sớm nhất từng ghi nhận 16/8/2003) — Dân Trí"
  - "Nhiệt độ thấp nhất đợt này: Bắc Bộ/Bắc Trung Bộ phổ biến 21-24 độ C, vùng núi cao Bắc Bộ có nơi dưới 19 độ C — Dân Trí"
  - "Đêm 9-10/9, Bắc Bộ mưa rào dông rải rác 10-30mm, cục bộ trên 70mm — Dân Trí"
  - "Kịch bản áp thấp/bão kết hợp không khí lạnh, 10-11/9: Tây Nguyên & Nam Bộ mưa 60-120mm cục bộ trên 180mm; Thanh Hoá-Huế 40-100mm cục bộ trên 150mm; duyên hải Nam Trung Bộ 15-30mm cục bộ trên 80mm — Dân Trí + Tuổi Trẻ (khớp 2 nguồn)"
  - "Từ 12-17/9, các tỉnh Trung Bộ nguy cơ cao lốc, sét, lũ quét, sạt lở đất, ngập úng cục bộ — Dân Trí + Tuổi Trẻ"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chủ đề chọn từ Google Trends VN nhóm A2 ưu tiên (thời tiết/thiên tai đưa trung lập, khuyến cáo an toàn, dẫn nguồn cơ quan chức năng, KHÔNG khai thác thương vong — đây thuần là bản tin dự báo/cảnh báo, chưa có thiệt hại xảy ra). Các chủ đề trending khác trong khung giờ đã xét và loại theo GATE A: 'giám đốc' (tin nhân sự Vingroup có khung 'vì sao rời ban lãnh đạo' mời suy đoán cá nhân — cận đời tư/drama), 'bệnh viện e' (cáo buộc/điều tra đang diễn ra liên quan cá nhân cụ thể), 'phú quang' (đời tư thừa kế gia đình người nổi tiếng đã mất), các trận đấu bóng đá châu Âu/MLS và 'lionel messi'/'casemiro' (thể thao nước ngoài thuần giải trí không yếu tố VN), 'ukraina' (xung đột vũ trang/đối ngoại), 'iphone 16 pro max'/'airpod 5' (trùng chủ đề Apple đã dựng 2 video liên tiếp gần đây, traffic thấp, không có góc mới). Style dựng: 7-timeline-chronology (index 6, lần đầu dùng trong vòng xoay của tuyến này). Tổng thời lượng thiết kế 59.83s / render thật 59.833333s. Verify 4 bước: (1) ffprobe 59.833333s khớp thiết kế; (2) ffmpeg silencedetect -35dB/0.6s — không phát hiện khoảng lặng chết; (3) trích frame tại 3.5/9/26/29.5/43/47.5/56.5s, xem bằng Read — đúng thiết kế, không phần tử bịa, cân bằng dọc đạt (đã sửa hook — tăng padding/tag-margin để khớp dải phân bố tham chiếu — và data-moment — tăng khoảng cách DƯỚI/19°C để hết content_overlap); (4) transcript Gemini gemini-flash-lite-latest (gemini-flash-latest bị 429 hết quota free-tier request/phút, chuyển sang lite) — khớp SCRIPT.md 7/7 dòng nội dung, chỉ có nhầm âm gần giống do ASR (số đọc thành chữ, 'lũ quét' nghe thành 'lốc quét' — lỗi nhận dạng giọng nói do âm gần giống với 'lốc' xuất hiện ngay trước đó trong câu, không phải lỗi viết tắt/đọc lắp của giọng đọc)."
```
