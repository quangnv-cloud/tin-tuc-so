# COMPLIANCE — gia-dien-giam-2-phan-tram
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-31T13:45:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN (A2 — chính sách giá điện/thuế xăng, đưa nội dung chỉ đạo, không bình luận chính trị; framing "chỉ đạo/dự kiến")
trending_signal: "giá điện — Google Trends VN, vị trí 8 trong list, 1000+ (cùng chủ đề: 'điện' vị trí 36, 500+); có ở cả category=news (Tuổi Trẻ 8ca6a0ebf217, Dân Trí 34f9cf18fab0)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Dân Trí (công nhân điện lực), có dẫn nguồn 'Tuổi Trẻ, Dân Trí' trong video; nhạc nền Google Lyria tự sinh, không lời (không dùng fallback ElevenLabs Music); SFX từ repo; giọng AI narrator chung (Vbee Minh Quân, tài khoản GỐC)"
claims_verified:
  - "Chính phủ chỉ đạo EVN rà soát, tiết giảm chi phí, hướng tới giảm giá bán lẻ điện khoảng 2% đến hết 31/3/2027; Phó thủ tướng Nguyễn Văn Thắng, sáng 31/10 trước Quốc hội — Tuổi Trẻ + Dân Trí (đối chiếu 2 nguồn)"
  - "Giá bán lẻ bình quân hiện hành 2.204,0655 đ/kWh (chưa VAT) từ 10/5/2025; giảm 2% từ 1/11 dự kiến còn ~2.159 — Tuổi Trẻ (dự kiến, EVN chưa công bố)"
  - "Giá thành 2025 2.092,70 đ/kWh; giá bán cao hơn 111,37 đ = 5,32% — Tuổi Trẻ"
  - "Thuế tiêu thụ đặc biệt xăng 7%→0% tháng 11 đến hết năm, ~4.000 tỷ; cùng giảm giá điện tạo dư địa ~0,07 điểm %; CPI 9 tháng +4,52% — Tuổi Trẻ + Dân Trí (đối chiếu 2 nguồn)"
  - "10 năm qua tăng 6 lần, chưa lần giảm; lần giảm duy nhất 20 năm cho mọi đối tượng, trừ 5 đợt thời Covid gần 17.000 tỷ — Tuổi Trẻ (1 nguồn, dẫn rõ 'Theo Tuổi Trẻ')"
  - "Phép tính riêng, suy ra từ số trong nguồn: 2.204 − 2.159 ≈ 45 đồng/kWh (hiển thị '−45đ')"
sensitive_flags: ["chính sách giá điện/lạm phát — framing trung lập, nêu rõ mới là chỉ đạo/dự kiến, cần theo dõi thông báo chính thức của EVN/Chính phủ"]
vietnam_legal_flags: []
notes: "Voice Vbee tài khoản GỐC (từ 31/10 theo quy định; biến TẠM không có). BGM Lyria. Transcript (Gemini flash-latest) khớp SCRIPT. Loudnorm: -13.8 LUFS, TP -1.6 dBTP (bản render gốc -20.9 LUFS nên đã tăng gain + alimiter). Render 1080x1920/30fps, 71.7s. Góc riêng (B7): quy mức giảm 2% thành -45 đồng/kWh, đặt cạnh giá thành điện, lạm phát và lịch sử 10 năm không giảm. Act 5 đã bỏ số liệu CPI khỏi lời đọc nhưng vẫn hiển thị (có trong nguồn). Thumbnail có caption karaoke lọt khung (không ảnh hưởng nội dung)."
