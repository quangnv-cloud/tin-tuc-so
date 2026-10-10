# COMPLIANCE — samsung-loi-nhuan-ky-luc-80-ty-usd
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-10T06:55:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN  (A2: kinh tế/doanh nghiệp trung lập + công nghệ; không khuyến nghị đầu tư)
trending_signal: ""   # chọn từ category=news (VnExpress Khoa học, id d23de466c338). Trending xét nhưng không dùng được: "động đất" (ảnh thumbnail 300x168, không có item news cùng chủ đề), "chứng khoán" (số liệu nguồn tự mâu thuẫn), "xăng"/"nghỉ hưu" (đã có video gần đây); còn lại là drama/hình sự/chính trị/thể thao nước ngoài.
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài VnExpress qua ?image=, có dẫn nguồn; giọng AI narrator chung (Vbee); nhạc Lyria tự sinh không lời; SFX trong repo"
claims_verified:
  - "Công bố 8/10; lợi nhuận hoạt động quý III ước 107,4 nghìn tỷ won (80,17 tỷ USD), gần 9 lần cùng kỳ — ?article=d23de466c338"
  - "Doanh thu 195 nghìn tỷ won, +127%; quý thứ 4 liên tiếp tăng vọt — ?article"
  - "Biên lợi nhuận gộp bán dẫn >80%; sản lượng HBM +gần 50% so với quý trước — ?article"
  - "Samsung và Micron: thiếu hụt tới 2028; mảng di động lỗ >1 tỷ USD; cổ phiếu -0,2%; báo cáo chi tiết 29/10 — ?article"
  - "Chỉ 1 nguồn (VnExpress, dẫn Reuters/LSEG); không có đối chiếu độc lập thứ hai — số liệu đều là ước tính do Samsung công bố"
sensitive_flags: ["Kinh tế/doanh nghiệp — số liệu là ước tính, chưa phải báo cáo chính thức (29/10); không khuyến nghị đầu tư"]
vietnam_legal_flags: []
notes: "Act 7 là câu hỏi quan điểm thật. Góc riêng (B7): hai mặt của cơn sốt chip nhớ (lãi mảng chip vs lỗ mảng di động). Hạn chế QC: act 3/5/6 kết thúc ~1270-1340px (dưới ngưỡng 1400 của brand), phần dưới có caption karaoke; loudness cuối -14,6 LUFS."
