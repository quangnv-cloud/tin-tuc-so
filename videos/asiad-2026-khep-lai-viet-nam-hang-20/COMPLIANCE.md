# COMPLIANCE — asiad-2026-khep-lai-viet-nam-hang-20

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-04T06:52:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "đoàn the thao việt nam — vị trí #4/60 (index 3) trong list category=trend, trafficApprox 200+; related: Dân Trí (bảng xếp hạng + VĐV VN giành huy chương Asiad 20), Tuổi Trẻ (Việt Nam thất bại tại Asiad 20); có cả ở category=news (VnExpress Thể thao b764dbe3c8f8, e4affe231752; Tuổi Trẻ 53e370337389)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress (lễ trao huy chương kata đồng đội nữ), có dẫn nguồn trong card + badge, không chỉnh sửa nội dung; nhạc nền Google Lyria tự sinh (lyria-realtime-exp, instrumental) — KHÔNG dùng ElevenLabs Music fallback; giọng đọc Vbee 'HN - Minh Quân' (narrator chung); SFX bộ repo; logo + font Montserrat là tài sản kênh."
claims_verified:
  - "Việt Nam hạng 20: 3 HCV, 3 HCB, 19 HCĐ = 25 huy chương; sau Kuwait, trước Singapore; hai nội dung đua ngựa sáng 4/10 — VnExpress b764dbe3c8f8, khớp Tuổi Trẻ 53e370337389."
  - "Mục tiêu tối thiểu 4 HCV không đạt; Asiad 19 Hàng Châu cũng 3 HCV — VnExpress e4affe231752 + Tuổi Trẻ."
  - "HCV: kata đồng đội nữ 22/9 (thắng Iran 5-0), cầu mây đôi nữ 29/9 (thắng Philippines 2-0), cầu mây đội nữ 4 người 3/10 (thắng Thái Lan 2-1); 3 HCB: Nguyễn Thị Tâm, Đinh Văn Tâm, Châu Ngọc Tuyết Sang — VnExpress b764."
  - "Trung Quốc 169 HCV, Nhật Bản 83 HCV — VnExpress + Tuổi Trẻ. Thái Lan hạng 7 (18 vàng), Malaysia 11 (9), Indonesia 16 (5), Philippines 17 (4); VN hạng 5 Đông Nam Á — VnExpress (số vàng Indonesia/Philippines lấy theo VnExpress; bản Tuổi Trẻ ghi nhầm lẫn với số hạng nên không dùng)."
  - "Chỉ tiêu vàng không thành công: bắn súng, điền kinh, chèo thuyền, taekwondo, thể thao điện tử; điền kinh 1 HCĐ 4x400m hỗn hợp, kỷ lục quốc gia 3:14.54 — VnExpress e4af."
sensitive_flags: ["kết quả thể thao có yếu tố VN — chỉ nêu số liệu, phê bình kết quả không phê bình cá nhân"]
vietnam_legal_flags: []
notes: "A2 (thể thao có yếu tố VN). Câu 'chưa cho thấy sự tiến bộ' của Tuổi Trẻ chỉ nằm trong caption, có dẫn nguồn; không có trong voice. Phiên âm Gemini khớp SCRIPT (Kuwait đổi sang 'Cô-oét' trong SCRIPT sau khi ASR nghe thành 'cuba'). Karaoke caption: ElevenLabs STT hết quota (401 quota_exceeded) → timing từ khoá căn theo faster-whisper + phân bổ theo độ dài âm tiết (xấp xỉ). Acronym không có trong SCRIPT."
```

## Chi tiết
- GATE A: các từ khoá khác bị loại: bóng đá quốc tế không yếu tố VN (Argentina, Croatia–Anh, Mỹ–Mexico, Tây Ban Nha–Séc, Ấn Độ–Brasil, U-23 Hàn Quốc/Nhật/Trung Quốc), xổ số (cờ bạc), drama sao (Quang Lê), hình sự (Trương Mỹ Lan), nhân sự quân đội cấp cao (Hồ Quang Tuấn), mất điện cục bộ (không đủ tin), cảnh báo chuyển khoản/căn cước (nguồn thứ cấp giật gân).
- GATE B: B1 mọi số liệu truy về VnExpress/Tuổi Trẻ; B2–B3 không vi phạm, CTA là câu hỏi quan điểm thật; B4 ảnh thật có dẫn nguồn; B5 hợp lệ; B6 tiêu đề = sự kiện/số liệu; B7 góc riêng (3 vàng so với mục tiêu 4 và Asiad 19; lưới nước Đông Nam Á; nhìn theo môn); B8 không flag.
- GATE C: đã xem thumbnail + 12 frame; transcript khớp SCRIPT.
- Kỹ thuật: 1080×1920, 30fps, 68.6s, h264 + AAC; render `--quality high --video-bitrate 10M`, sau đó nén lại crf 25 + loudnorm 2-pass: -14.5 LUFS, True Peak -1.1 dBTP; silencedetect: chỉ 0.64s đuôi cuối video, không có lặng chết giữa video; mp4 ~4,9MB để Apps Script không hết bộ nhớ.

**decision: APPROVE**
