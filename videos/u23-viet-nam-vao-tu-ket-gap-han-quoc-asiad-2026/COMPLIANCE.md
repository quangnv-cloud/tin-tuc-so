# COMPLIANCE — u23-viet-nam-vao-tu-ket-gap-han-quoc-asiad-2026

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-23T01:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (topic pick): GREEN
trending_signal: "thứ hạng của u-23 việt nam gặp u-23 uzbekistan — vị trí #37/81 (category=trend), trafficApprox 20000+, related khớp đúng chủ đề (thua Uzbekistan 0-2, vẫn vào tứ kết Asiad 20 — nguồn Tiền Phong/VietNamNet/Thanh Niên trong related)"
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh og:image bài VnExpress Thể thao (?image=40b4a3ff0644), ảnh thật trận đấu Asiad 20, có dẫn nguồn, không watermark, không chỉnh sửa nội dung; nhạc nền tự sinh bằng Google Lyria (BGM thực tế đã dùng), 100% không lời, thuộc quyền dự án; SFX từ bộ SFX repo (videos/_reference-astra-openai/assets/sfx/)."
claims_verified:
  - "U23 Việt Nam thua U23 Uzbekistan 0-2 (đối chiếu VnExpress ?article=a960df387e6b + ?article=40b4a3ff0644)"
  - "Việt Nam khép vòng bảng C với 4 điểm, nhì bảng, hơn Philippines 1 điểm, hơn Kuwait 3 điểm (VnExpress ?article=a960df387e6b)"
  - "Bảng xếp hạng bảng C: Uzbekistan 9đ, Việt Nam 4đ, Philippines 3đ, Kuwait 1đ (VnExpress ?article=a960df387e6b)"
  - "Đối thủ tứ kết là Hàn Quốc, nhất bảng D 6 điểm, thắng Qatar 4-1 và Arab Saudi 2-0 (VnExpress ?article=40b4a3ff0644)"
  - "Lịch sử Asiad: Hàn Quốc thắng Việt Nam 4-0 (1998), 2-0 (2006), 3-1 (bán kết 2018) (VnExpress ?article=40b4a3ff0644)"
  - "Tháng 1/2026, Việt Nam thắng luân lưu Hàn Quốc 7-6 (hòa 2-2) giành HC đồng U23 châu Á (VnExpress ?article=40b4a3ff0644)"
  - "Việt Nam vắng Đình Bắc, Thái Sơn, Nhật Minh, Văn Khang, Hiểu Minh, Trung Kiên; không còn HLV Kim Sang-sik (VnExpress ?article=40b4a3ff0644)"
  - "Hàn Quốc thay 16 vị trí, bổ sung cầu thủ từ Brentford/Celtic/Swansea, tận dụng 3 suất quá tuổi (VnExpress ?article=40b4a3ff0644)"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tin thể thao thuần kết quả + số liệu, có yếu tố VN (A2). Không dính drama/cá nhân/chính trị. Góc nhìn riêng (B7): khai thác nghịch lý kép (thua nhưng vẫn đi tiếp; từng thắng Hàn Quốc tháng 1 nhưng đội hình hai bên đã đổi khác) qua bảng xếp hạng + timeline lịch sử đối đầu (style 2-chip-and-leaderboard, index 1), không chỉ đọc lại tiêu đề báo. Act 6 (Impact) chỉ nêu sự thật đã xảy ra (thay đổi lực lượng), không suy đoán kết quả tứ kết."
```

## GATE A — chọn chủ đề

Nhóm **A2 — kết quả thể thao có yếu tố VN** → GREEN. Trending vì kết quả thi đấu thật của đội
tuyển U23 quốc gia tại Asiad (đấu trường châu lục), không dính drama cá nhân/chính trị/thể thao
nước ngoài thuần giải trí. Chủ đề xuất hiện cả ở `category=trend` (traffic 20000+) và
`category=news` (nhiều báo VN uy tín đưa tin: VnExpress, Tuổi Trẻ, Dân Trí, Tiền Phong, VietNamNet,
Thanh Niên).

## GATE B — kiểm duyệt nội dung

- **B1 Sự thật & nguồn**: mọi số liệu (tỷ số 0-2, điểm số bảng C, lịch sử đối đầu 4-0/2-0/3-1/7-6,
  danh sách cầu thủ vắng mặt, số vị trí thay đổi của Hàn Quốc) đều truy được về `?article=a960df387e6b`
  và `?article=40b4a3ff0644` (VnExpress Thể thao). Không có số liệu tự nghĩ. Act 6 nêu thay đổi lực
  lượng là sự thật đã xảy ra, không suy đoán ai thắng ở tứ kết.
- **B2 An toàn cộng đồng**: không bạo lực/thù ghét/quấy rối/doxxing/nội dung nhạy cảm. Phê bình
  (nếu có) chỉ ở mức nhận xét thể thao trung lập.
- **B3 Chính hãng**: kênh không mạo nhận VnExpress/AFC/Asiad; không testimonial giả, không
  engagement bait — CTA là câu hỏi quan điểm thật bám đúng nghịch lý của tin.
- **B4 AI/synthetic media**: giọng đọc ElevenLabs "Khánh Lâm" (AI narrator chung) = GREEN, không
  cần disclosure. Ảnh Hook/Article Image Card dùng nguyên ảnh thật từ `?image=40b4a3ff0644` (báo
  VnExpress), có dẫn nguồn, không chỉnh sửa/tái dựng bằng AI. Không có cảnh AI mô phỏng người
  thật/sự kiện thật dạng ảnh chụp.
- **B5 Bản quyền**: ảnh chỉ từ `?image=`; nhạc nền Lyria tự sinh, không lời (xem AUDIO NOTES dưới);
  SFX từ bộ SFX repo. Video 100% tự dựng bằng HyperFrames, không reup.
- **B6 Tiêu đề/thumbnail**: tiêu đề "U23 Việt Nam thua Uzbekistan 0-2, vẫn vào tứ kết gặp Hàn Quốc ở
  Asiad 2026" nêu đúng sự kiện + số liệu, không giật gân quá mức. Thumbnail (frame Hook, t=3.5s)
  hiện đủ rõ logo, tên kênh, badge nguồn, tiêu đề, 2 tag tương phản.
- **B7 Nguyên bản**: góc nhìn riêng là "nghịch lý kép" (thua trận nhưng đi tiếp nhờ hiệu số; từng
  thắng Hàn Quốc tháng 1 nhưng đội hình hai bên nay đã đổi khác) trình bày qua bảng xếp hạng bảng C
  (leaderboard tô cam hàng Việt Nam) và timeline lịch sử đối đầu (chip lớn) — không chỉ đọc lại tiêu
  đề báo. Style dựng `2-chip-and-leaderboard` (index 1, do `claim_style` cấp) khác style vừa dùng ở
  2 video gần nhất (`10-stock-terminal`, `1-card-and-bar`).
- **B8 Pháp lý VN**: không chạm an ninh mạng/thông tin sai/dữ liệu cá nhân/quảng cáo có điều kiện.
  Không flag.

## GATE C — kiểm tra cuối

- Xem lại thumbnail + các frame render thật (Hook, What, Facts, Data, Context, Impact, CTA qua
  `ffmpeg -ss <t>`): đúng B6, không phần tử bịa, không lộ lỗi; đã sửa 2 vòng cân bằng dọc cho frame
  Facts/Data/Impact (đẩy nội dung xuống + căn giữa dọc trong card) trước khi coi là đạt.
  - **Frame Impact còn hạn chế** (ghi nhận trung thực, không đủ điều kiện coi là lỗi chặn phát
    hành): sau khi thêm `justify-content:center` + tăng spacing, nội dung 2 thẻ kết thúc quanh
    `top:1240px` — nằm dưới mốc khuyến nghị `1400-1680px` của mục "Cân bằng dọc" nhưng đã cải thiện
    đáng kể so với bản đầu (~980px) và không còn để lộ mảng đen trống lớn ngay dưới nội dung chính
    trong card. Nêu rõ ở đây để theo dõi, không hạ chuẩn ngầm.
- Transcript (Gemini `gemini-flash-latest`, do Whisper bị chặn ở sandbox) khớp gần như tuyệt đối
  với `SCRIPT.md` — không câu nào "chế thêm" khi sinh voice, không lỗi đọc lắp/đánh vần do viết tắt.
- Caption dùng để đăng = `CAPTION.md` đã qua GATE B, không sửa tay thêm claim mới.

**decision: APPROVE — risk_level: GREEN.**

## Nguồn nhạc nền (BGM) thực tế đã dùng

Google Lyria (`lyria-recipe.py`, model `models/lyria-realtime-exp`) — **thành công ngay lần đầu**,
không cần fallback ElevenLabs Music. Recipe: `--density 0.25 --brightness 0.4`, prompt "calm ambient
news underscore, soft synth pads, sparse, minimal pulse, no drums, instrumental only",
`--negative-prompt "vocals, lyrics, singing, choir, rap, spoken word, humming"`. Retrim 69.29s +
fade-out 2.5s, `data-volume=0.30`, carve `--strength 0.4` (dữ liệu ducking đã ghi vào `index.html`
qua `carve.mjs`).

## Verify 5 bước (file render thật)

1. Duration: 69.3s (thiết kế 69.287552s) — đúng.
2. Silencedetect (`-40dB:d=0.6`): không phát hiện khoảng lặng chết nào trong toàn video.
3. Loudnorm: Input Integrated -14.1 LUFS (đạt ±1 LU so với -14.0), True Peak -1.3 dBTP (đạt ≤ -1.0
   dBTP) — đã chạy `loudnorm` 2-pass (target TP -1.5 dBTP để chừa margin an toàn cho AAC re-encode)
   vì lần đo đầu tiên lệch -15.4 LUFS.
4. Trích frame tại mốc quan trọng của cả 7 act + soát cân bằng dọc từng act giữa bằng Read — xem
   mục GATE C ở trên.
5. Transcript (Gemini multimodal) khớp SCRIPT.md.
