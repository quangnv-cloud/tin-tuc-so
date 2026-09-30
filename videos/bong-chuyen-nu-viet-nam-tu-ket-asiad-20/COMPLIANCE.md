# COMPLIANCE — bong-chuyen-nu-viet-nam-tu-ket-asiad-20

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-20T07:20:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "bóng chuyền nữ — trafficApprox 2000+ (Google Trends VN, xuất hiện ở cả trend và news cùng ngày)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài báo VnExpress Thể thao (assets/img/article-hero.jpg, id a9fb3290cdc9), có dẫn nguồn trong card + badge; không chỉnh sửa nội dung ảnh; nhạc nền sinh bằng Google Lyria (lyria-recipe.py, calm/instrumental, negative-prompt loại vocal); SFX từ bộ repo chung; logo public/logo.png và font Montserrat là tài sản thương hiệu kênh."
claims_verified:
  - "Việt Nam thua Hàn Quốc 1 set thắng – 3 set thua (19-25, 21-25, 28-26, 18-25), lượt cuối vòng bảng D Asiad 20, chiều 18/9/2026 — đối chiếu VnExpress Thể thao (?article=a9fb3290cdc9), khớp tiêu đề VietNamNet + Dân Trí trong related."
  - "Vì thua, Việt Nam xếp nhì bảng D, phải gặp Trung Quốc (đương kim vô địch 2 kỳ Á vận hội liên tiếp) ở tứ kết ngày 20/9/2026 — nguồn VnExpress Thể thao."
  - "Set 3: Việt Nam bỏ lỡ liên tiếp 5 cơ hội kết thúc set, thắng ở lần thứ 6 với tỷ số 28-26 — nguồn VnExpress Thể thao (đã sửa lỗi soạn thảo ban đầu nhầm thành 'cứu 5 set-point', xác minh lại đúng nghĩa gốc trước khi sinh voice/dựng hình)."
  - "Đội hình chính: HLV Nguyễn Tuấn Kiệt, đội trưởng Trần Thị Thanh Thúy, cùng Võ Thị Kim Thoa, Trần Thị Bích Thủy, Bùi Thị Ánh Thảo, Phạm Quỳnh Hương — nguồn VnExpress Thể thao."
  - "Lịch sử đối đầu: năm 2023 (Asiad 19 + giải châu Á) Việt Nam thắng Hàn Quốc 2 lần; 2 trận gần nhất trước 18/9/2026 đều thua — nguồn VnExpress Thể thao."
sensitive_flags: []
vietnam_legal_flags: []
notes: "Video tường thuật kết quả thể thao đội tuyển quốc gia (A2 — có yếu tố VN rõ ràng), không đụng đời tư/hình sự/chính trị. Không có claim nào ngoài nguồn báo; số liệu đối chiếu khớp related snippets của VietNamNet/Dân Trí cùng chủ đề."
```

## Chi tiết kiểm tra

### GATE A — chọn chủ đề
Từ khoá **"bóng chuyền nữ"** (Google Trends VN, `id c52cc3de20af`, `trafficApprox` 2000+) xuất hiện đồng
thời ở `category=news` với bài đúng chủ đề (VnExpress Thể thao, `id a9fb3290cdc9`). Nhóm **A2 — kết quả
thể thao có yếu tố VN** (đội tuyển quốc gia thi đấu Á vận hội). Đã loại các chủ đề khác cùng khung giờ
thuộc A1 (chính trị "tô lâm", hình sự "bị can"/"cướp"/"bắt giữ", xổ số "xsmb/xsmt/xsmn", thể thao nước
ngoài không yếu tố VN — UFC/Ngoại hạng Anh/Serie A/Bundesliga/Ligue 1/La Liga/Liga MX) và các từ khoá
rác/quá chung chung. Chi tiết đầy đủ ở `BRIEF.md`. → **GREEN**.

### GATE B — nội dung (SCRIPT.md + CAPTION.md + ảnh, trước render)
- **B1 Sự thật & nguồn**: mọi số liệu (tỷ số từng set, tổng tỷ số, số cơ hội bỏ lỡ, tên đội hình, lịch
  sử đối đầu 2023) đều truy được về bài VnExpress Thể thao dùng làm nguồn chính, đối chiếu khớp tiêu đề
  VietNamNet + Dân Trí trong `related`. Phát hiện và sửa 1 lỗi diễn đạt trong bản nháp đầu (dòng data
  moment ghi nhầm "cứu 5 set-point" — ngụ ý Việt Nam phòng thủ trước đối thủ — trong khi nguồn gốc là
  Việt Nam **tự bỏ lỡ** 5 cơ hội kết thúc set của chính mình trước khi thắng ở lần thứ 6; đã sửa lại
  đúng nghĩa gốc trong SCRIPT.md, BRIEF.md, CAPTION.md và trong composition (`04-data.html`) trước khi
  sinh voice/render). Không có con số nào tự bịa ngoài nguồn.
- **B2 An toàn cộng đồng**: không bạo lực/thù ghét/quấy rối/doxxing/nội dung 18+. Nội dung thuần thể
  thao, không công kích cá nhân — chỉ tường thuật kết quả và nhận định chuyên môn trung lập.
- **B3 Chính hãng**: kênh không mạo nhận là VnExpress hay bất kỳ cơ quan/hãng nào; badge "Nguồn:
  VnExpress" đúng thực tế. Không testimonial/dashboard giả, không engagement bait — CTA là câu hỏi
  quan điểm thật bám sát tình huống trận đấu.
- **B4 AI/synthetic media**: giọng ElevenLabs "Khánh Lâm" (narrator chung, không giả giọng người thật)
  = GREEN, không cần disclosure. Ảnh Hook + Article Image Card dùng ảnh thật từ bài báo, có dẫn nguồn,
  không chỉnh sửa nội dung = GREEN. Không có cảnh AI tái dựng người/sự kiện thật như ảnh chụp — mọi đồ
  hoạ khác (trục thời gian, thẻ số liệu, icon CSS) là minh hoạ ý niệm rõ ràng.
- **B5 Bản quyền**: ảnh chỉ từ `?image=` (không watermark), nhạc Lyria tự sinh (instrumental, có
  negative-prompt loại vocal), SFX từ bộ repo chung, video 100% tự dựng.
- **B6 Tiêu đề/thumbnail**: tiêu đề "Bóng chuyền nữ Việt Nam thua ngược Hàn Quốc, gặp Trung Quốc ở tứ
  kết Asiad 20" = sự kiện + số liệu, không giật gân. Thumbnail (Hook, t=4.0s) phản ánh đúng nội dung —
  đã xem lại, logo/tên kênh/badge nguồn/tiêu đề/2 tag đều rõ, không mờ/cắt.
- **B7 Nguyên bản**: góc nhìn riêng — khung "5 cơ hội kết thúc set bị bỏ lỡ" làm data moment (thay vì
  chỉ đọc lại tỷ số chung cuộc) + trục thời gian đối đầu Hàn Quốc từ 2023 (Context) cho góc nhìn lịch sử
  mà báo gốc không nhấn mạnh. Style dựng (7-timeline-chronology) khác các video gần đây (Style-based
  card/bar, split-comparison...). CTA đặt câu hỏi tranh luận thật bám tình huống ("tạo bất ngờ trước
  Trung Quốc hay dừng bước").
- **B8 Pháp lý VN**: không chạm an ninh mạng/thông tin sai/dữ liệu cá nhân/quảng cáo có điều kiện —
  không flag.
→ **GREEN** (1 lỗi diễn đạt phát hiện và sửa trước khi sinh voice/render, không phải "YELLOW-fixed sau
render" — sửa xong trước khi tốn công dựng nên tính là GREEN sạch).

### GATE C — kiểm tra cuối (sau render, trước đăng)
- Đã xem lại `output/thumbnail.jpg` + 4 frame trích từ video thật (what-happened, key-facts, context,
  CTA) bằng Read (multimodal): đúng B6, không phần tử bịa, không lỗi hiển thị, cân bằng dọc đạt (nội
  dung mỗi act kết thúc trong khoảng top 1450–1650px, đo bằng phân tích pixel thực tế trên preview
  trước khi render — không chỉ ước lượng mắt thường).
- Transcript (Gemini `gemini-flash-latest`, đối chiếu SCRIPT.md): khớp đủ 7 dòng, không câu nào "chế
  thêm"; chỉ có sai khác nhỏ do nhận dạng giọng nói (không ảnh hưởng nội dung thật của video, vì
  composition dùng đúng file voice đã sinh từ SCRIPT.md, không phải transcript).
- Caption dùng để đăng = `CAPTION.md` đã qua GATE B, không sửa tay thêm claim mới.
- Verify kỹ thuật (độc lập, tự chạy lại chứ không chỉ tin báo cáo dựng video):
  - `ffprobe` duration: 61.6s (khớp thiết kế `data-duration=61.503061` + làm tròn render).
  - `ffmpeg silencedetect -40dB/0.6s`: không phát hiện khoảng lặng chết nào giữa video.
  - `ffmpeg loudnorm`: Input Integrated **-14.1 LUFS**, True Peak **-1.0 dBTP** (đạt chuẩn -14 LUFS
    ±1 LU, TP ≤ -1.0 dBTP — đã qua 1 lần chỉnh loudnorm 2-pass do bản đo đầu lệch -15.4 LUFS).
  - 1080×1920, h264/30fps, AAC 192kbps/48kHz stereo — đúng chuẩn xuất bản cố định.

**decision: APPROVE — đủ điều kiện đăng Facebook Reel + YouTube Shorts.**
