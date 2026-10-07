# COMPLIANCE — tach-truyen-tai-dien-khoi-evn
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-07T14:00:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): YELLOW (A3 — chính sách/tái cơ cấu doanh nghiệp nhà nước; là định hướng trong đề án, chưa phải quyết định ban hành → framing "định hướng/đề xuất", nêu cần theo dõi nguồn chính thức)
trending_signal: "tập đoàn điện lực việt nam / vị trí 2 trên 134 trong category=trend / ~200+; đồng thời có 3 bài cùng chủ đề trong category=news (Dân trí, VnExpress)"
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh og:image Dân trí qua ?image= (684x456), có dẫn nguồn 'Nguồn: Dân trí' + nhãn 'Ảnh bài báo · Dân trí'; nhạc nền Google Lyria tự sinh (không lời; ElevenLabs Music KHÔNG dùng vì hết quota nhưng Lyria thành công nên không cần fallback); SFX bộ repo; giọng AI narrator Vbee chung (không giả người thật); không ảnh AI tái dựng cảnh thật"
claims_verified:
  - "họp báo Bộ Công Thương chiều 7/10; ông Bùi Quốc Hùng, Phó cục trưởng Cục Điện lực — khớp ?article= Dân trí c810f3f324fe, VnExpress 8c0f260ef957, Tuổi Trẻ"
  - "định hướng sớm tách EVNNPT khỏi EVN, chuyển về bộ ngành quản lý; tách bạch 4 khâu phát điện/truyền tải/phân phối/bán lẻ — khớp Dân trí + VnExpress"
  - "truyền tải, phân phối = độc quyền tự nhiên (không thể xây nhiều đường dây song song); phát điện, bán buôn, bán lẻ có thể cạnh tranh — khớp Dân trí + VnExpress"
  - "EVN sở hữu hơn 40% các dự án, nguồn phát điện — khớp Dân trí"
  - "đơn vị điều độ hệ thống điện (NSMO) đã tách khỏi EVN, chuyển về Bộ Công Thương — khớp VnExpress, Tuổi Trẻ"
  - "đề án định hướng tiếp tục thoái vốn Nhà nước tại 5 tổng công ty phát điện thuộc EVN — khớp VnExpress (gán cho 'đề án', không gán cho Bộ Công Thương)"
  - "đề án trình Chính phủ 15/9 cùng đề án tái cơ cấu EVN do Bộ Tài chính xây dựng — khớp Tuổi Trẻ (ghi nguồn trên hình)"
  - "9 tháng đầu năm công suất nguồn điện tăng ~3,5%, thấp hơn mục tiêu 6,6%; nguyên nhân Bộ nêu: thủ tục chấp thuận/chọn nhà đầu tư, đất đai-giải phóng mặt bằng, đàm phán hợp đồng mua bán điện, cơ chế giá — khớp VnExpress"
  - "trích dẫn '…cần tách bạch các khâu phát điện, truyền tải, phân phối và bán lẻ điện' — nguyên văn lời ông Hùng trong Dân trí"
sensitive_flags: ["chính sách tái cơ cấu doanh nghiệp nhà nước — framing trung lập, nêu rõ là định hướng; không suy đoán tác động giá điện; act 6 chỉ nêu số liệu đã xảy ra"]
vietnam_legal_flags: ["tái cơ cấu doanh nghiệp nhà nước / sửa Luật Điện lực dự kiến trình Quốc hội — nêu theo bài báo, không trích số điều luật; cần theo dõi thông báo chính thức của Bộ Công Thương và Chính phủ"]
notes: "B7 góc riêng: chuỗi cung ứng điện 4 khâu, phân định khâu độc quyền tự nhiên / cạnh tranh, tỉ lệ sở hữu nguồn phát điện của EVN và bối cảnh tiến độ nguồn điện chậm (3,5% vs 6,6%) — không chỉ đọc lại tiêu đề. Style 9-editorial-clipping (claim_style index 8). Caption karaoke căn mốc theo độ dài từ + khoảng lặng phát hiện bằng silencedetect (ElevenLabs STT hết quota). Transcript Gemini (gemini-3-flash-preview) khớp SCRIPT. Loudness sau loudnorm 2-pass: -14.7 LUFS, true peak -1.9 dBTP. Kèm bản nén nhẹ -fb.mp4 (3,2MB) phòng Apps Script hết bộ nhớ với bản gốc 31MB."
