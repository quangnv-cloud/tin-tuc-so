# COMPLIANCE — asiad-20-viet-nam-ngay-1-10
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-01T14:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN  (A2 — thể thao có yếu tố Việt Nam, tường thuật kết quả)
trending_signal: "đại hội thể thao châu á / vị trí #5 trong list category=trend / trafficApprox 2000+ (cùng chủ đề có ở category=news: Dân Trí 8c822ee73ddb)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image Dân Trí (?image=8c822ee73ddb), ghi 'Ảnh: Dân Trí' + badge nguồn, không chỉnh sửa nội dung; giọng đọc AI narrator chung (Vbee HN - Minh Quân); nhạc nền Google Lyria tự sinh (không lời; không cần fallback ElevenLabs Music); SFX từ repo; video 100% tự dựng."
claims_verified:
  - "1/10: huy chương duy nhất trong ngày là HCĐ Liên minh huyền thoại, thua Đài Loan (Trung Quốc) 0-2 ở bán kết — Dân Trí ?article"
  - "Thống kê Dân Trí: 2 HCV, 1 HCB, 19 HCĐ"
  - "Phạm Quang Huy hạng 4, 25m súng ngắn nam, 20 điểm, kém HCĐ 1 điểm (số 21 trên biểu đồ suy ra từ 'kém một điểm')"
  - "Phùng Thị Huệ jujitsu 48kg nữ: thua bán kết 2-4, thua tranh HCĐ 4-6"
  - "Đặng Công Đức: thắng tứ kết, thua bán kết, thua VĐV Ấn Độ ở trận tranh HCĐ cung ba dây nam"
  - "Cầu mây quadrant nữ toàn thắng vòng bảng vào bán kết; quadrant nam thua Ấn Độ 0-2; bóng chuyền nam thắng Uzbekistan 3-0 vào vòng tranh hạng 9-12"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Một nguồn chính (Dân Trí; các báo VOV/VietNamNet chỉ đối chiếu tiêu đề do snippet rỗng) — mọi claim là kết quả thi đấu, không gây tranh cãi. Voice Vbee 7/7; transcript Gemini khớp SCRIPT (một lần model đọc nhầm 'hai mươi' thành 'mười chín', hai lần hỏi lại có chủ đích đều xác nhận 'hai mươi'; 'Sát nhất' nghe thành 'Tiếc nhất' - gần âm, không đổi nghĩa số liệu). Caption karaoke tính theo độ dài giọng (ElevenLabs STT không dùng). Loudness -14.6 LUFS, TP -1.3 dBTP (loudnorm 2-pass). Góc riêng (B7): 'bảng khoảng cách tới huy chương'. Đã tải ảnh/bài qua Apps Script; có 1 lần curl trực tiếp trang Dân Trí chỉ để đọc meta description (trái khuyến nghị, không dùng làm nguồn). Push lên nhánh claude/kind-tesla-1xp01d theo chỉ định của phiên, không phải master."
