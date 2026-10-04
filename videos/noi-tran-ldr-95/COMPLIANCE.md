# COMPLIANCE — noi-tran-ldr-95

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-04T00:50:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "ngân hàng — #1 trong list category=trend, trafficApprox 500+; related: VnExpress/CafeF/Dân Trí về Thông tư mới & nới trần LDR 95%; có cả ở category=news (Dân Trí id 35f5d235e4b4, VnExpress Kinh doanh id 33a41df4b519)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Dân Trí, có dẫn nguồn trong card + badge, không chỉnh sửa nội dung, không xoá watermark; nhạc nền Google Lyria tự sinh (instrumental) — KHÔNG dùng ElevenLabs Music fallback; giọng đọc Vbee 'HN - Minh Quân' (narrator chung); SFX bộ repo; logo + font Montserrat là tài sản kênh."
claims_verified:
  - "Thông tư 50/2026 (NHNN) hiệu lực từ 1/12/2026; trần LDR 85% → 95%; 100 đồng huy động: tối đa 85 → 95 đồng — ?article=35f5d235e4b4 (Dân Trí), khớp VnExpress (VnExpress ghi nhầm 'lên 100 đồng' trong 1 câu, mâu thuẫn với trần 95% cùng bài → dùng 95)."
  - "Hai chỉ tiêu LCR/NSFR; chỉ ngân hàng đăng ký tuân thủ đồng thời mới áp trần 95%; chưa đăng ký sớm vẫn trần 85% trước 10/2028 — VnExpress ?article=33a41df4b519."
  - "Lộ trình: bắt buộc từ 10/2028, đăng ký sớm từ cuối năm nay; NSFR 100% từ 10/2030; LCR 100% từ 10/2033; cả hai 100% thì hết giới hạn LDR (vẫn báo cáo) — Dân Trí + VnExpress."
  - "MBS Research: đến 28/9 dư nợ tín dụng ≈ 20,6 triệu tỷ đồng, +13,2% so với đầu năm — Dân Trí (số 11,6%/20,75 triệu tỷ ở bài khác là cách tính khác, không dùng)."
  - "27 ngân hàng MBS theo dõi: LDR cuối quý II +2,55 điểm % so với đầu năm, vẫn dưới trần 85%; MBS: không đồng nghĩa mở rộng tín dụng không giới hạn — Dân Trí + VnExpress."
sensitive_flags: ["tin tài chính — chỉ nêu quy định đã ban hành + nhận định có dẫn nguồn MBS, không khuyến nghị đầu tư/cổ phiếu"]
vietnam_legal_flags: []
notes: "Chính sách đã ban hành (A2). Không drama/hình sự/chính trị. Whisper + Gemini phiên âm khớp SCRIPT (sai lệch chỉ do nhận dạng 'MB' → 'Maybank' và 'Chỉ' → 'Khi', đã nghe lại bằng 2 lượt ASR khác nhau cho kết quả đúng). Acronym 'MBS/LCR/NSFR/LDR' chỉ xuất hiện ở text hiển thị, SCRIPT dùng dạng đọc đầy đủ."
```

## Chi tiết
- GATE A: các từ khoá khác bị loại: bóng đá quốc tế không yếu tố VN (Croatia–Anh, Tây Ban Nha–Séc, Thái Lan–Philippines…), xổ số/Vietlott (cờ bạc), đời tư/drama (Quang Lê – Phương Mỹ Chi), hình sự (Trương Mỹ Lan), nhân sự quân đội cấp cao (Hồ Quang Tuấn), mất điện cục bộ (không đủ tin).
- GATE B: B1 mọi số liệu truy được về Dân Trí/VnExpress; B2–B3 không vi phạm, CTA là câu hỏi quan điểm thật; B4 ảnh thật có dẫn nguồn; B5 hợp lệ; B6 tiêu đề = sự kiện/số liệu; B7 góc riêng (quy đổi 100 đồng huy động, điều kiện đăng ký sớm, trục lộ trình 2026–2033); B8 không flag.
- GATE C: đã xem thumbnail + frame cả 7 act; transcript khớp SCRIPT.
- Kỹ thuật: 1080×1920, 30fps, 66.3s, h264 + AAC; loudnorm 2-pass: -14.6 LUFS, True Peak -1.1 dBTP; silencedetect 0 khoảng lặng chết; mp4 nén lại ~3,4MB để Apps Script không hết bộ nhớ.

**decision: APPROVE**
