# COMPLIANCE — chung-khoan-viet-nang-hang-ban-rong

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-09T02:20:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "cổ phiếu — vị trí #19/42 trong danh sách Google Trends VN lúc phát hiện, trafficApprox 500+, pubDate 2026-09-08T08:40:00Z. Chủ đề (nâng hạng chứng khoán VN / khối ngoại bán ròng) xuất hiện ở CẢ category=trend (từ khoá "cổ phiếu") VÀ category=news (nhiều bài chứng khoán/cổ phiếu cùng ngày)."
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card = og:image bài Dân Trí (id 3b4d8ebd4c73, ?image= endpoint), có dẫn nguồn 'Nguồn: Dân Trí' trong Brand Anchor + caption 'Ảnh: Dân Trí' trong card — không chỉnh sửa nội dung ảnh. Nhạc nền do Lyria tự sinh (instrumental, không lời, negative-prompt vocals đã áp dụng), retrim + fade-out theo đúng tổng thời lượng thật. SFX từ thư viện repo (chime/click-soft/impact-bass/pop/whoosh-short). Không dùng asset nào khác ngoài repo/API đã cấu hình. Giọng đọc ElevenLabs 'Khánh Lâm' — AI narrator chung, không giả giọng người thật cụ thể."
claims_verified:
  - "FTSE Russell nâng hạng chứng khoán Việt Nam từ cận biên lên mới nổi thứ cấp, hiệu lực 21/9/2026 — đối chiếu ?article=3b4d8ebd4c73 (Dân Trí)"
  - "Lộ trình 4 giai đoạn 9/2026-9/2027, tỷ trọng luỹ kế 10%/30%/65%/100%, đợt 21/9 chỉ áp hệ số 10% — đối chiếu ?article=3b4d8ebd4c73"
  - "VN-Index chiều 8/9 quanh 1.827 điểm, tăng hơn 5 điểm, phục hồi sau phiên giảm 31 điểm đầu tuần — đối chiếu ?article=3b4d8ebd4c73 và ?article=e08a02244920 (Tuổi Trẻ)"
  - "Khối ngoại bán ròng hôm nay >350 tỷ đồng; 4 phiên gần nhất >2.300 tỷ đồng; luỹ kế 8 tháng đầu năm >90.000 tỷ đồng trên HOSE — đối chiếu ?article=3b4d8ebd4c73"
  - "Riêng tháng 8 chỉ bán ròng 1.357 tỷ đồng, thấp hơn bình quân 13.600 tỷ đồng/tháng của tháng 6-7 — đối chiếu ?article=3b4d8ebd4c73"
  - "Trích dẫn ông Đinh Minh Trí (Giám đốc Phân tích KHCN, Mirae Asset) và ông Nguyễn Tiến Dũng (Trưởng phòng Nghiên cứu, MBS) — nguyên văn nhận định trong bài, không diễn giải thêm kết luận ngoài nguồn"
sensitive_flags: []
vietnam_legal_flags:
  - "Tin tài chính/chứng khoán — KHÔNG đưa khuyến nghị mua/bán, chỉ tường thuật số liệu công khai + nhận định đã công bố của chuyên gia có tên, chức danh, công ty rõ ràng. Không thuộc diện quảng cáo tài chính có điều kiện."
notes: |
  Nội dung sản xuất bởi routine tự động "Tin Tức Số" (khung TỐI 20h20). Chủ đề chọn theo mục 1.c/1.d
  ROUTINE.md: trùng cả category=trend ("cổ phiếu") và category=news (nhiều bài cùng chủ đề); nguồn
  thật chốt là Dân Trí (id 3b4d8ebd4c73, KHÔNG ghi "Google Trends" là nguồn). Style đã claim qua
  Apps Script: index 0 = "1-card-and-bar". Góc nhìn riêng (B7): nghịch lý "tin vui nâng hạng vs khối
  ngoại vẫn bán ròng" — không chỉ đọc lại tiêu đề báo.

  Verify kỹ thuật (4 bước, đều đạt):
  1) ffprobe duration = 64.77s (thiết kế 64.75s, dưới 75s) — khớp.
  2) ffmpeg silencedetect noise=-35dB:d=0.6 — CHỈ có 1 khoảng lặng tại 64.08s→64.77s (đúng đoạn
     fade-out cuối act CTA sau khi voice + nhạc kết thúc), KHÔNG có khoảng lặng chết giữa video.
  3) Trích frame tại giữa/cuối mỗi act (t=3,10,15,20,29,33.5,39,43,50,55,60) — xem bằng Read: brand
     đúng (#FF5A1F/#0B0E14, logo Tin Tức Số góc trên-phải, "Nguồn: Dân Trí" góc trên-trái), bar chart
     Data moment tô đúng màu (cột luỹ kế 90.000 tỷ tô cam, 2 cột phụ màu xám theo đúng Style 0), cân
     bằng dọc đạt ở trạng thái ổn định cuối mỗi act (nội dung kết thúc trong khoảng top ~1420-1540px,
     không trống đen nửa dưới) — không phần tử bịa, không emoji trong composition.
  4) Transcript (Gemini multimodal, model gemini-flash-lite-latest — Whisper bị chặn egress, model
     gemini-flash-latest/gemini-3.8-flash bị 429 quota free-tier) khớp SCRIPT.md sát nghĩa từng câu,
     "FTSE Russell" và "VN-Index" được đọc/nhận dạng đúng, không có câu nào bị "chế thêm", không lỗi
     đọc lắp do viết tắt.

  npm run check: 0 errors/0 warnings (Lint/Runtime/Motion), Layout 0 issues/9 samples, Contrast 49/49
  WCAG AA pass.

  Lưu ý vận hành: bước sản xuất kỹ thuật ban đầu chạy qua 1 agent nền, bị dừng giữa chừng ở bước
  verify do rate-limit phiên (không phải lỗi nội dung/kỹ thuật) — phiên này đã tiếp tục và tự hoàn
  tất toàn bộ bước verify còn lại (silencedetect, trích frame, transcript, thumbnail) trực tiếp trước
  khi ký GATE C.
