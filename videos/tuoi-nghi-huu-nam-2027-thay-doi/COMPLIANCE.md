# COMPLIANCE — tuoi-nghi-huu-nam-2027-thay-doi
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-14T07:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "nghỉ hưu" (Google Trends VN, id 5e63b9a43ddb, trafficApprox 500+, vị trí #3/256 trong danh sách mới nhất, pubDate 2026-09-14T05:10:00Z); trùng khớp với item category=news cùng ngày (Dân Trí, id 5b61c4ab36d8) — chọn theo ưu tiên "có ở cả trend và news". Nhóm A2 (chính sách mới đã ban hành — lộ trình tuổi nghỉ hưu theo luật hiện hành, không phải đề xuất/tranh luận chính trị).

Các chủ đề trending khác đã xét trong khung giờ này và loại (theo BRIEF.md): "hoài linh" (đời tư/tin đồn nghệ sĩ — A1), "santos laguna đấu với juarez" và hàng loạt trận bóng đá châu Âu/Mỹ (thể thao nước ngoài thuần giải trí không yếu tố VN — A1), "bitcoin"/"binance" (tài chính tiền số dễ dính khung "kèo" — rủi ro A1), "vũ hồng việt" (traffic cao bất thường nhưng không rõ ngữ cảnh, có thể liên quan cá nhân cụ thể — không đủ thông tin để verify an toàn, bỏ qua), "công ty tnhh mtv tư vấn đầu tư gfdi" (liên quan vụ án lừa đảo đầu tư đang xử lý — A1 cáo buộc hình sự), "18 pro max"/iPhone (trùng chủ đề với video gần đây trên kênh — bỏ để đa dạng nội dung), "ios 27" (an toàn nhưng ưu tiên "nghỉ hưu" vì vừa trending vừa có ở category=news cùng ngày, và kênh vừa có nhiều video Apple liên tiếp).

GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card: og:image bài báo Dân Trí (tải qua ?image=5b61c4ab36d8), dùng nguyên trạng không chỉnh sửa nội dung, có dẫn nguồn (Brand Anchor + badge Hook + CAPTION). Nhạc nền: Google Lyria tự sinh (instrumental, đã xác nhận 100% không lời qua Gemini multimodal), quyền thuộc dự án. SFX: bộ palette có sẵn trong repo (_reference-astra-openai/assets/sfx/), không chỉnh tốc độ/pitch để né Content ID. Giọng đọc: ElevenLabs AI narrator chung (Khánh Lâm), không giả giọng người thật cụ thể."
claims_verified:
  - "Tuổi nghỉ hưu 2027: nam 61 tuổi 9 tháng, nữ 57 tuổi 4 tháng — đối chiếu BRIEF.md mục Nội dung chính"
  - "Mức tăng so với 2026: nam +3 tháng, nữ +4 tháng — đối chiếu BRIEF.md"
  - "Điều kiện hưởng lương hưu: đóng BHXH bắt buộc từ đủ 15 năm trở lên — đối chiếu BRIEF.md (Luật BHXH 2024)"
  - "Mốc 2021: nam 60 tuổi 3 tháng, nữ 55 tuổi 4 tháng — đối chiếu BRIEF.md"
  - "Mốc 2026: nam 61 tuổi 6 tháng, nữ 57 tuổi 0 tháng — đối chiếu BRIEF.md"
  - "Đích lộ trình: nam 62 tuổi từ 2028, nữ 60 tuổi từ 2035 — đối chiếu BRIEF.md"
  - "Lương hưu tối đa 75% bình quân lương — nữ sau 30 năm đóng, nam sau 35 năm đóng — đối chiếu BRIEF.md"
  - "Công thức cộng thêm: 2%/năm (nữ), 1%/năm (nam) sau mốc tối thiểu, tới trần 75% — đối chiếu BRIEF.md (diễn giải lại công thức 45%+2%/năm nữ và 45%(20 năm)/40%(15 năm)+1%/năm nam quy về cách nói đơn giản 'mỗi năm thêm')"
  - "Nguồn: Báo Dân Trí, 14/9/2026 — đối chiếu BRIEF.md mục Nguồn"
sensitive_flags: []
vietnam_legal_flags: []
notes: |
  - Style dựng: 9-editorial-clipping (claim_style index 8) — style CHƯA từng dùng trong log trước đây,
    tự dựng HTML/CSS/GSAP mới hoàn toàn theo mô tả CONSTRUCTION-STYLES.md mục "Style 8 — Editorial
    Clipping" + phần suy diễn (mục 6.9) của TECHNICAL-CONSTRUCTION-GUIDE.md: ảnh bài báo cắt dán xoay
    nhẹ có viền trắng + "băng dán", dấu ngoặc kép khổng lồ mờ phía sau con số chính, gạch chân tay-vẽ
    (SVG path không đều) dưới con số, 3 "mẩu giấy" xếp chồng lệch góc có bóng ở Key facts, pull-quote
    block (border-left dày) cho trục thời gian ở Context, 2 "mẩu báo" chồng một phần ở Impact.
  - Góc nhìn riêng (B7): tổng hợp lộ trình rải rác trong bài gốc thành 1 trục so sánh rõ ràng
    2021→2026→2027→đích 2028/2035, và giải thích công thức tính % lương hưu theo giới — không chỉ đọc
    lại tiêu đề báo.
  - Thời lượng video: 66.63s (dưới trần 75s).
  - Verify 4 bước (PRODUCTION-WORKFLOW.md mục 7):
    (1) ffprobe duration = 66.633333s, khớp thiết kế (root data-duration=66.63).
    (2) ffmpeg silencedetect -35dB/0.6s: không có khoảng lặng chết GIỮA video; khoảng lặng duy nhất
        phát hiện là 65.28s→66.65s (1.37s) — đúng vùng fade-out BGM cuối video, bình thường.
    (3) Trích frame gần CUỐI mỗi act (không phải giữa act, theo bài học mục 7.2/7.3
        TECHNICAL-CONSTRUCTION-GUIDE.md) bằng ffmpeg độc lập từ file .mp4 đã render, xem bằng Read
        tool cho cả 7 act: Hook (t=5.5s), What (13.5s), Facts (21.0s), Data (28.2s), Context (44.5s),
        Impact (54.3s), CTA (60.95s). Tất cả đạt cân bằng dọc (phần tử cuối kết thúc trong khoảng
        top:1400-1680px hoặc tương đương tỷ lệ trên khung 1920px), không phần tử bịa, không lộ tĩnh,
        đúng brand màu #FF5A1F/#0B0E14/#FF4438, Montserrat, không emoji trong composition.
    (4) Transcript: Gemini multimodal (gemini-flash-latest) liên tục trả lỗi 503 "high demand" sau 5
        lần thử với backoff — chuyển sang `python -m whisper` cục bộ (model "small", language
        Vietnamese) làm phương án thay thế hợp lệ theo PRODUCTION-WORKFLOW.md. Transcript full audio
        khớp SCRIPT.md ở mọi số liệu/mốc (2027, +3 tháng nam/+4 tháng nữ, 15 năm, 61t9th nam/57t4th
        nữ, 2021: 60t3th, đích 62 tuổi 2028/60 tuổi 2035, 75%, 30 năm nữ/35 năm nam) — không câu nào
        "chế thêm", không lỗi đọc lắp/đánh vần do viết tắt lọt vào script. Riêng nghi vấn ban đầu ở
        dòng 6 (model whisper "base" nghe nhầm "30 năm" của nữ thành "35 năm") đã tự loại trừ: chạy
        lại riêng line6.mp3 bằng model whisper "small" (chính xác hơn) cho kết quả đúng "nữ 30 năm ·
        nam 35 năm", xác nhận đây là artefact ASR chất lượng thấp của model "base", không phải lỗi
        thật của giọng đọc.
  - Bug kỹ thuật phát hiện + đã sửa trong vòng QC đầu (trước khi chốt bản render cuối):
    (a) 02-what.html: div "wh-caption" còn sót lại nhưng class CSS đã đổi tên, khiến dòng "Nguồn: Báo
        Dân Trí..." hiện không định vị (position) đè lên góc trên khung — đã gộp vào trong panel dưới
        class "wh-panel-source" đúng vị trí, đồng thời tăng kích thước panel để lấp khung dọc tốt hơn.
    (b) 04-data.html: CSS selector ".dm-num" (div cha, có opacity:0 mặc định) và GSAP target "#dm-num"
        (span con) là 2 phần tử khác nhau → số "61" bị ẩn vĩnh viễn dù đã chạy tween xong (chỉ thấy
        "tuổi 9 tháng" phóng to). Đã sửa bằng cách gộp class+id vào cùng 1 phần tử; verify lại bằng
        frame render thật xác nhận "61" hiển thị đúng, không còn content_overlap trong npm run check.
    (c) 06-impact.html: 2 "mẩu báo" chồng lên nhau ban đầu overlap quá sâu khiến dòng chữ cuối của thẻ
        phía sau (nữ, "...hiểm xã hội") bị thẻ phía trước (nam) cắt ngang giữa chừng — đã tăng khoảng
        cách top giữa 2 thẻ để chỉ chồng nhẹ ở phần không có chữ, vẫn giữ hiệu ứng chiều sâu vật lý.
    (d) 05-context.html: đẩy toàn bộ 4 dòng pull-quote (trục thời gian) xuống ~30-100px mỗi dòng để
        phần tử cuối (mốc đích 2028/2035) kết thúc trong dải an toàn 1400-1680px thay vì dừng sớm hơn.
    Đã render lại toàn bộ sau khi sửa, `npm run check` sạch 0 error, và verify lại đủ 4 bước + cân
    bằng dọc trên bản render cuối cùng ở trên.
