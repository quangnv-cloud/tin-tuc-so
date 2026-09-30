# BRIEF — tuoi-nghi-huu-2027-thay-doi

## Chủ đề & nguồn
- **Trending signal**: từ khoá "bảo hiểm xã hội" (Google Trends VN, id `d08ce802734d`, vị trí #1/142
  trong danh sách `category=trend` lúc chạy routine, `trafficApprox` "2000+", `pubDate`
  2026-09-16T05:20:00.000Z).
- **Nguồn bài chính dùng cho `?article=`**: id trend `d08ce802734d` → server tải `related[0]` =
  "Năm 2027, tuổi nghỉ hưu sẽ thay đổi ra sao?", **Báo Thanh Niên**
  (`thanhnien.vn/nam-2027-tuoi-nghi-huu-se-thay-doi-ra-sao-18526091516245845.htm`). Bài trích dẫn cụ
  thể Bộ luật Lao động 2019 và Luật Bảo hiểm xã hội 2024 (hiệu lực 1/7/2025).
- **Nguồn đối chiếu thứ 2**: `category=news`, id `0e2bfb2595f7`, **Dân Trí**, "Đóng bảo hiểm xã hội
  tự nguyện 17 năm, xin hưởng lương hưu sớm được không?" — trong bài có mục con "Tuổi nghỉ hưu của
  người lao động năm 2027 thay đổi ra sao?" xác nhận ĐỘC LẬP đúng số liệu "năm 2027 tuổi nghỉ hưu lao
  động nam tăng 3 tháng, nữ tăng 4 tháng", đồng thời trích dẫn cụ thể Điều 98 Luật Bảo hiểm xã hội,
  Khoản 2 Điều 169 Bộ luật Lao động, Nghị định 159/2025/NĐ-CP cho điều kiện 15 năm đóng bảo hiểm xã
  hội. Hai nguồn khớp nhau về số liệu chính.
- **Ảnh**: item `trend` (`?image=d08ce802734d`) chỉ trả thumbnail Google rất nhỏ (275×183) — theo
  đúng PRODUCTION-WORKFLOW §1.9/ROUTINE §5, dùng ảnh báo chuẩn từ item `category=news` cùng chủ đề:
  `?image=0e2bfb2595f7` (Dân Trí, ảnh báo chí thật 1280×853, cảnh cán bộ bảo hiểm xã hội tư vấn người
  dân tại một cửa hàng tạp hoá — minh hoạ đúng chủ đề "bảo hiểm xã hội/lương hưu" ở mức tổng quát,
  KHÔNG gắn với 1 số liệu cụ thể nào trong video nên không gây hiểu sai).

## GATE A
Nhóm **A2 — chính sách/quy định đã ban hành (lương, bảo hiểm xã hội)**: đây là lộ trình tăng tuổi
nghỉ hưu đã được quy định từ Bộ luật Lao động 2019 (không phải đề xuất mới/tranh cãi), tiếp tục có
hiệu lực sang năm 2027; không đụng cá nhân, không phải tin đồn/drama, không chính trị/bầu cử. →
**GREEN**.

## Số liệu đã xác minh (đối chiếu 2 nguồn: Thanh Niên + Dân Trí)
- Từ năm 2027, tuổi nghỉ hưu điều chỉnh theo lộ trình Bộ luật Lao động 2019: lao động nam tăng thêm
  3 tháng, lao động nữ tăng thêm 4 tháng so với năm 2026. — Thanh Niên + Dân Trí (khớp nhau)
- Năm 2027: lao động nam nghỉ hưu khi đủ 61 tuổi 9 tháng; lao động nữ nghỉ hưu khi đủ 57 tuổi 4
  tháng. — Thanh Niên
- Lộ trình tăng dần dừng lại khi nam đạt 62 tuổi (năm 2028), nữ đạt 60 tuổi (năm 2035). — Thanh Niên
- Điều kiện hưởng lương hưu (theo Luật Bảo hiểm xã hội 2024, hiệu lực 1/7/2025): đủ tuổi nghỉ hưu +
  đóng bảo hiểm xã hội bắt buộc từ đủ 15 năm trở lên. — Thanh Niên; xác nhận độc lập bởi Dân Trí
  (trích Điều 98 Luật Bảo hiểm xã hội, Khoản 2 Điều 169 Bộ luật Lao động).
- Người làm nghề nặng nhọc/độc hại/nguy hiểm hoặc làm việc ở vùng có điều kiện kinh tế - xã hội đặc
  biệt khó khăn: được nghỉ hưu sớm hơn, tối đa 5 năm so với tuổi quy định. — Thanh Niên
- Riêng người làm công việc khai thác than trong hầm lò, có từ đủ 15 năm làm công việc này: được
  nghỉ hưu sớm hơn tối đa 10 năm. — Thanh Niên

**Không dùng**: đề xuất "tăng tuổi nghỉ hưu công chức lên 70" (Bộ Nội vụ mới đang tham khảo kinh
nghiệm nước ngoài, chưa ban hành) — loại khỏi video để tránh nhầm giữa đề xuất và quy định đã có
hiệu lực (giữ đúng B1: phân biệt đề xuất/dự đoán vs sự thật đã xác nhận).

## Ảnh
`assets/img/article-hero.jpg` — ảnh báo thật lấy qua `?image=0e2bfb2595f7` (Dân Trí), gốc 1280×853,
không chỉnh sửa nội dung. Nguồn hiển thị trên video (Brand Anchor + Hook badge + CAPTION) = "Dân
Trí" — vì ảnh và 1 trong 2 nguồn xác minh đều từ Dân Trí, tránh lệch nguồn hiển thị so với ảnh.

## Style dựng
`claim_style` trả **index 4 — `5-map-and-geo`** (bản đồ — địa lý). Chủ đề chính sách lao động toàn
quốc không có tâm điểm địa lý rõ như thiên tai/khu vực, nên diễn giải ẩn dụ bản đồ theo đúng 2 yếu
tố địa lý CÓ THẬT trong nguồn: (1) phạm vi áp dụng toàn quốc của lộ trình tuổi nghỉ hưu, (2) ngoại lệ
địa lý/nghề nghiệp thật trong luật — "vùng có điều kiện kinh tế - xã hội đặc biệt khó khăn" và "khai
thác than hầm lò" được nghỉ hưu sớm hơn. KHÔNG bịa thêm tên tỉnh/vùng cụ thể không có trong nguồn —
bản đồ chỉ gắn nhãn chung "vùng đặc biệt khó khăn" như luật viết, không chỉ đích danh địa phương nào.
- What happened: ảnh + panel, ghim địa danh nhỏ nhãn "Toàn quốc" cạnh badge nguồn.
- Key facts: bản đồ Việt Nam outline mờ phía sau 2 fact card lớn (nam 61 tuổi 9 tháng / nữ 57 tuổi 4
  tháng năm 2027 — đúng nội dung dòng thoại 3).
- Data moment: mốc DỪNG của lộ trình (đúng nội dung dòng thoại 4) — con số chính "62" (tuổi, mốc dừng
  của nam, đạt năm 2028) trong 1 map-pin phóng to, chip phụ bên dưới cho nữ "60 tuổi" (mốc dừng, năm
  2035).
- Context: ẩn dụ "hành trình tới lương hưu" trên 1 trục dọc kiểu tuyến đường có 2 điểm dừng (pin) +
  1 điểm đến — đúng nội dung dòng thoại 5 (điều kiện hưởng lương hưu): điểm dừng 1 "đủ tuổi nghỉ hưu
  theo quy định", điểm dừng 2 "đóng bảo hiểm xã hội bắt buộc từ đủ 15 năm", điểm đến "được hưởng
  lương hưu hằng tháng" — trục vẽ dần tô cam đậm dần khi tới đích, giữ đúng ẩn dụ địa lý (tuyến
  đường/waypoint) mà không bịa thêm địa danh cụ thể ngoài nguồn.
- Impact: 2 thẻ trượt vào từ 2 hướng (trái/phải), nền bản đồ mờ full-frame — đúng nội dung dòng thoại
  6 (nghỉ hưu sớm theo đặc thù nghề/vùng, đã ban hành, không suy đoán): "nghề nặng nhọc/độc hại + vùng
  đặc biệt khó khăn: sớm tối đa 5 năm" và "khai thác than hầm lò (đủ 15 năm làm nghề): sớm tối đa 10
  năm".

**Lưu ý đối chiếu nội dung–giọng đọc**: mỗi act giữa dựng đúng số liệu của DÒNG THOẠI riêng act đó
(không lặp/lấn số liệu của act khác) — Key facts (dòng 3) = 61t9th/57t4th; Data moment (dòng 4) =
mốc dừng 62/60; Context (dòng 5) = điều kiện 15 năm đóng bảo hiểm xã hội; Impact (dòng 6) = nghỉ hưu
sớm 5-10 năm.

## Góc nhìn riêng (B7)
Không chỉ đọc lại tiêu đề "tuổi nghỉ hưu tăng" — tổng hợp đủ 3 lớp thông tin từ luật (mốc tuổi cụ thể
theo giới tính, điều kiện số năm đóng bảo hiểm xã hội, và các trường hợp ngoại lệ nghỉ hưu sớm theo
nghề/vùng) thành 1 bức tranh đầy đủ hơn từng bài hỏi-đáp đơn lẻ trên báo, đối chiếu độc lập 2 nguồn
(Thanh Niên + Dân Trí) khớp số liệu, và đặt câu hỏi tranh luận thực chất đang được người lao động
quan tâm mỗi khi lộ trình tăng tuổi hưu bước sang năm mới.

## CTA
Câu hỏi: "Tuổi nghỉ hưu tiếp tục tăng theo lộ trình đã định — bạn thấy đây là điều chỉnh cần thiết
để đảm bảo quỹ bảo hiểm xã hội, hay sẽ tạo thêm áp lực cho người lao động?" — 2 lựa chọn đối lập:
"Cần thiết để đảm bảo quỹ" (mũi tên lên cam) vs "Áp lực với người lao động" (tam giác cảnh báo đỏ).
