# COMPLIANCE — viet-nam-nguoc-dong-pakistan-asean-cup

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-02T14:05:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "việt nam vs pakistan — #6 trong list category=trend, trafficApprox 50000+ (viet nam vs pakistan 20000+, fpt play 10000+); có cả ở category=news (Tuổi Trẻ id f488e2a3c259, VnExpress Thể thao)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Tuổi Trẻ (khung tĩnh từ GIF), có dẫn nguồn trong card + badge, không chỉnh sửa nội dung; nhạc nền Google Lyria tự sinh (instrumental) — KHÔNG dùng ElevenLabs Music fallback; giọng đọc Vbee 'HN - Minh Quân' (narrator chung); SFX bộ repo; logo + font Montserrat là tài sản kênh."
claims_verified:
  - "Việt Nam 4-2 Pakistan, lượt cuối bảng B FIFA ASEAN Cup 2026, 2/10, sân Gelora Bung Karno (Jakarta); Pakistan dẫn 1-0 hiệp 1 — ?article=f488e2a3c259 (Tuổi Trẻ), khớp VnExpress."
  - "50' Hai Long 1-1; 57' Hoàng Đức 2-1; 80' Đình Bắc 3-1; 88' Ali Akbar Khan 2-3; 90+1' Williams Minh Hoàng 4-2; Đình Bắc 1 bàn 2 kiến tạo, vào sân đầu hiệp 2 cùng Tuấn Tài — Tuổi Trẻ + VnExpress."
  - "Williams Minh Hoàng sinh 2007, bàn đầu tiên cho ĐTQG; hạng FIFA 99 vs 198; lời HLV Kim về thời tiết nóng — VnExpress."
  - "6 điểm (thắng Philippines 1-0, thua Thái Lan 0-2, thắng Pakistan 4-2), nhì bảng B, gặp Malaysia tranh hạng ba 5/10, chung kết Indonesia–Thái Lan — VnExpress."
  - "Suy ra từ diễn biến bàn thắng: hiệp 1 = 0-1, hiệp 2 = 4-1; Đình Bắc tham gia 3/4 bàn; biểu đồ hiệu số theo phút. Phút bàn mở tỷ số: hai báo lệch 31'/32' → biểu đồ dùng 31', script không nêu phút."
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tường thuật kết quả thể thao có yếu tố VN (A2). Không đời tư/hình sự/chính trị. ElevenLabs STT hết quota → mốc từ lấy bằng whisper cục bộ; transcript kiểm bằng Gemini (gemini-3-flash-preview) khớp SCRIPT, chỉ lệch do nhận dạng tên riêng."
```

## Chi tiết
- GATE A: các từ khoá khác đã loại: xổ số/vietlott (cờ bạc), thể thao nước ngoài (Thái Lan vs Philippines, Hàn Quốc vs Venezuela, Đan Mạch vs Bồ Đào Nha…), đời tư/drama (Đặng Lê Nguyên Vũ, Nana, Wang Xiyu), hình sự (vụ án, Trương Mỹ Lan, Nguyễn Thị Tâm đã làm sáng nay).
- GATE B: B1 mọi số liệu truy được về Tuổi Trẻ/VnExpress; B2–B3 không vi phạm, CTA là câu hỏi quan điểm thật; B4 ảnh thật có dẫn nguồn; B5 hợp lệ; B6 tiêu đề = sự kiện/số liệu; B7 góc riêng (tách 2 hiệp, hiệu số theo phút, Đình Bắc 3/4 bàn); B8 không flag.
- GATE C: đã xem thumbnail + frame cả 7 act; transcript khớp SCRIPT.
- Kỹ thuật: 1080×1920, 30fps, 64.9s, h264 + AAC 192k; loudnorm 2-pass: -14.6 LUFS, True Peak -1.1 dBTP; silencedetect 0 khoảng lặng chết.

**decision: APPROVE**
