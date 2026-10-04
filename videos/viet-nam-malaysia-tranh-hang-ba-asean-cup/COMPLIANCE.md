# COMPLIANCE — viet-nam-malaysia-tranh-hang-ba-asean-cup

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-04T14:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "kim sang-sik — vị trí #1/60 trong list category=trend, trafficApprox 1000+; related: Dân Trí, VietNamNet, Tạp chí Bóng đá; có cả ở category=news (VnExpress Thể thao 95bb63b8a730, e952f4843bb9; Tuổi Trẻ 50329b9f44f4)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress (cầu thủ Việt Nam số 13 ở FIFA ASEAN Cup), có dẫn nguồn 'Ảnh: VnExpress' + badge, không chỉnh sửa nội dung; nhạc nền Google Lyria tự sinh (instrumental) — KHÔNG dùng ElevenLabs Music; giọng đọc Vbee 'HN - Minh Quân' (narrator chung); SFX bộ repo; logo + font Montserrat là tài sản kênh."
claims_verified:
  - "Trận tranh hạng ba FIFA ASEAN Cup 2026 Việt Nam – Malaysia, 16h 5/10, sân Gelora Bung Karno (Jakarta) — VnExpress, Tuổi Trẻ, Dân Trí."
  - "Lần gần nhất Malaysia thắng VN: 4-2 tại Mỹ Đình 2014; từ đó thua 9, hòa 1; Tan Cheng Hoe 'không thắng họ hơn 10 năm qua' — VnExpress e952f4843bb9."
  - "VN thắng Malaysia tổng 4-0 hai lượt bán kết ASEAN Cup 2026; HLV Kim: đối thủ mạnh hơn rất nhiều — VnExpress 95bb63b8a730, Tuổi Trẻ 50329b9f44f4."
  - "Malaysia bảng A: 3-0 Bangladesh, 0-0 Indonesia, 6-0 Singapore, 7 điểm, ghi 9 bàn (Indonesia 11), chưa thủng lưới; VN thua Thái Lan 0-2 ngắt chuỗi 27 trận, thắng Pakistan 4-2 — VnExpress e952."
  - "Hoàng Hên không kịp hồi phục; Việt Anh chấn thương cơ đùi sau, cao 1m85, không hậu vệ nào khác của VN ở giải cao đến 1m80; tiền đạo Malaysia Tierney 1m86, Paulo Josue 1m83, Bergson 1m80 — Dân Trí (related của item trend). Malaysia vắng Dion Cools, Faisal Halim — Tuổi Trẻ, Dân Trí."
sensitive_flags: ["thông tin chấn thương cầu thủ — chỉ nêu theo báo chính thống, không suy đoán"]
vietnam_legal_flags: []
notes: "A2 (thể thao có yếu tố VN). Cố ý KHÔNG nêu vụ Malaysia bị FIFA/CAS xử lý nhập tịch. Karaoke caption: ElevenLabs STT hết quota (quota_exceeded) → timing căn theo silencedetect + phân bổ theo độ dài từ (xấp xỉ). BGM: Lyria thành công, không cần fallback ElevenLabs Music (cũng hết quota). Verify transcript: Gemini 3.6 (prompt verbatim, temp 0) + Whisper small khớp SCRIPT; một lần chạy Gemini 3.5 với prompt lỏng trả transcript bịa (tên/số liệu không có trong audio) — đã loại, không dùng. Loudness -14.4 LUFS, TP -1.3 dBTP; mp4 nén crf 25 (~4,9MB) để Apps Script không hết bộ nhớ."
```

## Chi tiết
- GATE A: các từ khoá khác bị loại: xổ số (cờ bạc), bóng đá quốc tế không yếu tố VN (Argentina, Anh–Croatia, Mỹ–Mexico, Tây Ban Nha–Séc…), drama sao (Quang Lê), "đe dọa", "mất điện" (cục bộ, nguồn mỏng), "vàng"/"tiền" (chung chung, dễ thành khuyến nghị đầu tư).
- GATE B: B1 số liệu truy về nguồn; B2–B3 không vi phạm, CTA là câu hỏi quan điểm thật; B4 ảnh thật có dẫn nguồn; B5 hợp lệ; B6 tiêu đề = sự kiện/số liệu; B7 góc riêng (con số 12 năm + 9 thua 1 hòa, so hành trình vòng bảng, so chiều cao hàng thủ–hàng công); B8 không flag.
- GATE C: đã xem thumbnail + 6 frame render; transcript khớp SCRIPT.
- Kỹ thuật: 1080×1920, 30fps, 65.3s, h264 + AAC; render `--quality high --video-bitrate 10M`; silencedetect không có lặng chết.

**decision: APPROVE**
