# COMPLIANCE — iphone-18-ra-mat-viet-nam

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-09T01:10:44Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "iphone 18 (Google Trends VN, vị trí #29/93 theo mới nhất, trafficApprox 500+)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Dân Trí (id 6ef106aee66f), có dẫn nguồn trong Hook + Article Image Card; nhạc nền sinh bằng Google Lyria (lyria-recipe.py, recipe calm, negative-prompt loại vocal), tự sinh cho dự án này; SFX từ bộ palette dùng chung của kênh (chime/click-soft/impact-bass-1/pop/whoosh-short)"
claims_verified:
  - "Sự kiện Apple 'Surprise and Shine', 9/9/2026, Apple Park — theo VnExpress"
  - "iPhone 18 Pro / iPhone 18 Pro Max ra mắt, kèm smartphone gập mới — BRIEF.md"
  - "Chip Apple A20 Pro, tiến trình 2nm — BRIEF.md/VnExpress (dẫn Instant Digital/TSMC)"
  - "Màn hình sáng hơn: 1.600 -> 3.000 nit — BRIEF.md/VnExpress"
  - "Bộ nhớ LPDDR5x 96-bit, GPU +20-30% — BRIEF.md/VnExpress (dẫn Digitimes)"
  - "Dự đoán giá tăng 100 (Cnet) / 150-200 (TrendForce) / 200 (IDC) / 250-300 (Jeff Pu) đô la Mỹ — BRIEF.md"
  - "Lịch trình: ra mắt 9/9, đặt hàng 12/9, người dùng đầu tiên 18/9, có thể lên kệ VN cùng ngày — BRIEF.md/VnExpress + đối chiếu Dân Trí"
  - "Giá chip nhớ 256GB tăng gần 400%/năm; chi phí sản xuất iPhone Pro 256GB +38% — BRIEF.md/VnExpress (dẫn TrendForce)"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Video đầu tiên của kênh Tin Tức Số. Style dựng: 2-chip-and-leaderboard (index 1, claim_style). Tổng thời lượng 74.85s thiết kế / 74.87s render thật — sát trần 75s vì tổng 7 dòng voice thật (eleven_v3, speed 1.09) đã dài 74.14s; đệm mỗi frame giảm còn ~0.1s (thay vì 0.3-0.5s khuyến nghị) để không vượt trần — quyết định có chủ đích, ưu tiên giới hạn tổng thời lượng cứng trong BRAND-SYSTEM.md over khuyến nghị đệm mềm. Verify 4 bước: (1) ffprobe 74.866667s; (2) silencedetect -35dB/0.6s — không phát hiện khoảng lặng chết; (3) trích frame tại 3.5/13/23.5/33/46/63/71.5s, xem bằng Read — đúng thiết kế, không phần tử bịa; (4) transcript Gemini (gemini-flash-latest + gemini-flash-lite-latest, transcribe từng dòng line1-7.mp3 riêng do lần đầu transcribe cả file ghép bị mô hình 'sửa' sai thành sự kiện iPhone 16 thật/It's Glowtime — hiện tượng hallucination của ASR khi ngữ cảnh dài trùng mẫu sự kiện thật đã biết; transcribe riêng từng dòng loại bỏ hoàn toàn hiện tượng này) khớp SCRIPT.md 7/7 dòng, chỉ 1 lỗi nhận dạng âm gần giống ở dòng 5 ('được cho là' nghe thành 'lực cho là' — lỗi ASR, không phải lỗi đọc của giọng)."
```
