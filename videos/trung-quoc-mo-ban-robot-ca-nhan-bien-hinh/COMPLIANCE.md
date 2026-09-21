# COMPLIANCE — trung-quoc-mo-ban-robot-ca-nhan-bien-hinh
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-21T07:08:11Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: ""
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/What-happened/Context là ảnh báo thật (og:image) lấy qua Apps Script `?image=f2fb4ddd2d1b` từ bài Tuổi Trẻ, có dẫn nguồn (badge + Brand Anchor \"Nguồn: Tuổi Trẻ\"), không chỉnh sửa nội dung ảnh, không bịa tình huống. Không dùng AI tái dựng cảnh thật/người thật — mọi đồ hoạ phụ (torn-paper note, quote mark, underline tay-vẽ, icon CSS/SVG) là hình khối CSS/SVG tự dựng. Nhạc nền tự sinh qua Google Lyria (không lời, instrumental), SFX lấy từ bộ SFX nội bộ repo (chime/click-soft/impact-bass-1/pop/whoosh-short), không dùng nhạc/SFX của bên thứ ba ngoài dự án. Giọng đọc ElevenLabs \"Khánh Lâm\" (voice_id RCmOaM1iiIH5xX3QXjIF) — giọng AI chung, không giả giọng người thật cụ thể."
claims_verified:
  - "Ngày ra mắt/mở bán: 20-9-2026 — khớp BRIEF.md + bài gốc Tuổi Trẻ (pubDate 2026-09-21T05:05:00.000Z tường thuật sự kiện ngày 20/9)."
  - "Công ty: Qiyuan Robotics, thuộc Tập đoàn Công nghệ vật liệu mới Thượng Vĩ (Shangwei New Material Technology) — khớp BRIEF.md."
  - "Hai mẫu robot: Qiyuan Q1 và Qiyuan T1 — khớp BRIEF.md, SCRIPT.md dòng 2."
  - "Qiyuan T1 chuyển đổi giữa dạng người có bánh xe và dạng bốn chân, hãng quảng bá \"robot cá nhân biến hình đầu tiên trên thế giới\" — khớp BRIEF.md (đã framing là tuyên bố hãng, không khẳng định tuyệt đối, đúng B1)."
  - "Qiyuan Q1 cao 88cm, gập lại bỏ vào ba lô, tuỳ chỉnh ngoại hình & một số bộ phận cấu trúc — khớp BRIEF.md."
  - "Thời gian lắp ráp & xuất xưởng mỗi robot: khoảng 2,5 phút, theo nhịp độ sản xuất/QC kiểu ô tô — khớp BRIEF.md, SCRIPT.md dòng 4."
  - "Giá: Q1 tiêu chuẩn 19.999 NDT (gần 3.000 USD), Q1 Explorer 26.999 NDT, T1 từ 19.999 NDT, T1 Pro 29.999 NDT — video dùng số khởi điểm 19.999 NDT / ~3.000 USD, khớp BRIEF.md (không bịa số)."
  - "Giao hàng dự kiến từ 1-10-2026 — khớp BRIEF.md, SCRIPT.md dòng 4."
  - "Phát ngôn CEO Điền Hoa (Tian Hua), giám đốc điều hành Tập đoàn Công nghệ vật liệu mới Thượng Vĩ, tại sự kiện \"Tôi và robot cá nhân của tôi\" — trích đúng nội dung BRIEF.md, không bịa thêm ý."
  - "Showroom trải nghiệm đầu tiên tại Thượng Hải, Quảng Châu, Thâm Quyến, Hàng Châu, Hạ Môn, Vũ Hán, Tây An — khớp BRIEF.md (liệt kê đủ 7 thành phố nêu trong nguồn, không thêm địa danh)."
  - "Ý nghĩa: robot cá nhân chuyển từ nghiên cứu/thử nghiệm sang sản xuất và bán thương mại đại trà — khớp BRIEF.md, là sự thật đã xảy ra (act Impact), không suy đoán tương lai."
sensitive_flags: []
vietnam_legal_flags: []
notes: "Chủ đề chọn từ category=news (không qua Google Trends VN — trending_signal để rỗng theo đúng quy ước). Lý do: quét trending sáng 21/9 chỉ toàn tra cứu chung/nhãn hiệu, thể thao nước ngoài thuần giải trí không yếu tố VN, xổ số (A1 cờ bạc), 1 mục chính trị nước ngoài và 1 mục nghi đời tư — không còn mục đạt A2/A3. Tin robot Qiyuan từ category=news khớp thẳng A2 (ra mắt sản phẩm/công nghệ), an toàn, có ảnh báo chuẩn, có phát ngôn chính thức lãnh đạo hãng, phù hợp style '9-editorial-clipping' đã claim. Đã đối chiếu toàn bộ số liệu/tên riêng/trích dẫn với BRIEF.md trước khi dựng script và composition. Transcript verify (Gemini gemini-flash-latest, vì whisper local bị chặn không cài được trong sandbox) khớp SCRIPT.md từng câu, chỉ lệch nhầm âm nhỏ được phép ('mốc' thay 'bước' ở dòng 6, '2' số thay 'hai' chữ ở dòng 1, '88 cm' thay '88 xăng-ti-mét' — đều không đổi nghĩa, không phải câu bịa thêm). Loudness đã chạy loudnorm 2-pass (I=-14 LUFS, TP=-1.5dBTP an toàn margin cho AAC re-encode) vì lần đo đầu -16.1 LUFS lệch quá ±1 LU so với chuẩn -14 LUFS. Cân bằng dọc đã verify bằng frame thật trích từ file render cho cả 7 act, phần tử cuối mỗi act nằm trong khoảng top 1450–1620px (xem báo cáo cuối phiên) — không có mảng đen trống nửa dưới khung."
