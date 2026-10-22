---
name: tao-21-reel
description: Tạo trọn 21 reel một tuần cho Quán Nhỏ Cuối Ngõ từ những đoạn sách Kioo dán vào. Tự rút ý đắt, ghi vào bảng ý, viết 3 khung sáng, trưa, tối, kiểm tra, biên tập, xuất CSV cho Canva. Dùng khi Kioo gõ /tao-21-reel.
disable-model-invocation: true
argument-hint: "[tuần, ví dụ 2026-W44, không bắt buộc] rồi dán các đoạn sách đã đọc"
---

# Tạo 21 reel cho một tuần

Kioo gọi: `/tao-21-reel` rồi dán các đoạn sách, mỗi đoạn ghi tên sách ở đầu nếu được. Có thể kèm cảm nghĩ riêng ("mình thấy...", "đoạn này làm mình nhớ...").

Nội dung Kioo gửi:

$ARGUMENTS

Đọc `CLAUDE.md` trước. Cách viết từng reel, định dạng file, độ dài và file CSV theo đúng `.claude/skills/lo-reel/SKILL.md`. Giọng chuẩn xem `.claude/skills/lo-reel/vi-du/lo-14-reel-dau.md`.

## Bước 1: Rút ý đắt từ đoạn sách

- Xác định tuần: lấy từ đầu nội dung nếu có dạng `2026-W44`, không có thì lấy tuần kế tiếp so với hôm nay. Nếu `lo/<tuần>/` đã có file thì hỏi Kioo trước khi ghi đè.
- Không ghi rõ tên sách thì đoán từ nội dung và nói rõ là đoán. Không đoán được thì hỏi.
- Mỗi đoạn rút 1 đến 4 ý. Một ý là một câu, viết lại bằng giọng quán, không chép nguyên văn.
- Chỉ rút ý có trong đoạn Kioo dán. Không thêm ý từ trí nhớ về cuốn sách.
- Làm dịu khi đoạn gốc:
  - chia người thành loại tốt và loại kém, hay phán xét người đang yếu: viết lại theo hướng "mình cũng từng như vậy";
  - hứa quá ("bất cứ điều gì bạn muốn", "thay đổi cuộc đời", "chắc chắn thành công"): bỏ phần hứa, giữ phần nhìn ra;
  - có con số hay ví von nghe như sự thật khoa học: giữ hình ảnh, bỏ con số.
- Cảm nghĩ riêng của Kioo đi kèm thì giữ lại, đó là chất liệu quý nhất cho reel kể chuyện và reel sách.
- Ghép thêm vào `du-lieu/y-dat.csv`, mã nối tiếp theo sách (A cho *Sức mạnh của tiềm thức*, B cho *Hiểu về trái tim*, chữ cái mới cho sách khác), cột `da_dung` để trống.

## Bước 2: Kiểm tra đủ ý chưa

- Một tuần cần khoảng 12 ý chưa dùng (cho 7 động viên, 6 kể chuyện, 2 sách; một ý có thể dùng cho 2 reel). Trích dẫn dùng câu cổ, không cần ý sách.
- Đủ: làm tiếp.
- Thiếu: vẫn làm, dùng lại ý cũ ít dùng nhất, và ghi rõ trong báo cáo cuối là thiếu bao nhiêu ý.
- Hai cuốn chủ lực nên cân nhau. Lệch nhiều thì nhắc Kioo đọc thêm cuốn còn lại.

## Bước 3: Lên bảng phân bổ trước khi viết

Lập một bảng 21 dòng (thứ, khung, loại, ý dùng, câu trích nếu có, sách cho comment ghim, nguồn clip) theo bảng phân bổ tuần trong skill `lo-reel`. Kiểm tra:

- Không ý nào dùng quá 2 lần trong tuần, hai reel cùng ý không đăng cùng ngày.
- 6 câu trích không trùng câu đã dùng trong `lo/`, xen kẽ tục ngữ, ca dao, triết gia phương Đông và phương Tây.
- Khoảng 6 reel ghi "Kioo tự quay", ưu tiên reel sách và kể chuyện.
- Câu mở không trùng các tuần trước.

## Bước 4: Viết 3 khung

Viết lần lượt `lo/<tuần>/sang.md`, `trua.md`, `toi.md`, mỗi file 7 reel, kèm `canva-sang.csv`, `canva-trua.csv`, `canva-toi.csv`.

- Viết từng khung một và đọc lại khung trước khi sang khung sau, để giọng không mòn và không lặp hình ảnh.
- Hook `kiem-tra-giong` chạy sau mỗi file. Sửa hết lỗi trước khi sang file kế.
- Reel sách: phần điều học được dùng cảm nghĩ của Kioo nếu có. Không có thì viết nháp và đánh dấu `[NHÁP - Kioo thay bằng điều thật]`.
- Reel kể chuyện: chỉ dựa vào hành trình Kioo đã kể (xem bài mẫu và cảm nghĩ Kioo gửi kèm). Chi tiết mới nào chưa chắc là thật thì đánh dấu `[Kioo xác nhận]`.

## Bước 5: Biên tập và ghi sổ

1. Gọi agent `bien-tap-vien` duyệt cả 3 file (có thể gọi 3 lần song song, mỗi lần một file). Áp dụng các đề xuất "Sửa", để lại đề xuất "Cân nhắc" cho Kioo.
2. Chạy lại `python3 .claude/hooks/kiem-tra-giong.py lo/<tuần>/*.md` để chắc không còn lỗi.
3. Ghi 21 dòng vào `du-lieu/theo-doi.csv`. Điền `da_dung` cho các ý đã dùng trong `du-lieu/y-dat.csv`.

## Bước 6: Báo lại Kioo

Ngắn gọn, theo thứ tự:

1. Đã xong 21 reel cho tuần nào, file nằm ở đâu.
2. Các ý mới đã thêm vào bảng, kèm chỗ đã làm dịu so với sách gốc.
3. Danh sách việc Kioo cần làm: 6 reel tự quay, các chỗ `[NHÁP]`, `[Kioo kiểm nguồn]`, `[Kioo xác nhận]`.
4. Các đề xuất "Cân nhắc" của biên tập viên.
5. Thiếu ý cho tuần sau không, nên đọc thêm cuốn nào.

Cuối cùng commit và push lên `main` để lô reel không mất khi session đóng. Ghi trong báo cáo là đã lưu lên GitHub.
