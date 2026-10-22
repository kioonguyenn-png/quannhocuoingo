# Quán Nhỏ Cuối Ngõ - sổ tay quán

Fanpage reel ngắn cho phụ nữ, cảnh đẹp và chill kèm một lời nhắc nhẹ, dẫn người xem về sách qua link affiliate ở comment ghim. Chủ quán là Kioo. Page đứng riêng, không liên quan Camellia413 Studio.

Kế hoạch đầy đủ: `tai-lieu/ke-hoach-fanpage.md`. Khi kế hoạch và sổ tay này lệch nhau, sổ tay này đúng.

## Nhịp đăng

- **3 reel mỗi ngày, 21 reel mỗi tuần.** Mỗi khung giờ một kiểu:

| Khung | Kiểu chính | Mở và đóng |
|---|---|---|
| Sáng | Động viên, một việc nhỏ làm ngay | "Chào bạn, sáng nay..." / "Uống ngụm nước rồi đi tiếp nhé." |
| Trưa | Trích dẫn (tục ngữ, ca dao, triết gia cổ) | Lời chào giữa ngày / một câu để lưu lại |
| Tối | Kể chuyện ngã rồi đi tiếp | Giọng radio đêm khuya / "Ngủ ngon nhé." |

- **Tỷ lệ một tuần (21 reel):** 7 động viên, 6 trích dẫn, 6 kể chuyện, 2 sách.
  - Sách đặt ở trưa thứ sáu và tối thứ ba (thay cho trích dẫn và kể chuyện hôm đó).
- Mỗi tuần khoảng 6 reel dùng clip Kioo tự quay (30%), còn lại clip AI hoặc stock đã chỉnh màu.

## Giọng

- Radio cũ, nữ tính, nhẹ nhàng. Như người dẫn chương trình đêm khuya đọc thư thính giả.
- Xưng "mình", gọi "bạn". Mình nói với mình, không dạy ai.
- Người trong cuộc: một người phụ nữ từng ngã nhiều lần trong kinh doanh và vẫn đang đi. Không nhắc loại hình kinh doanh.
- Câu ngắn. Phần lớn câu dưới 15 chữ, không câu nào quá 25 chữ.
- Tốc độ đọc khoảng 2,5 đến 3 chữ mỗi giây. 25 giây khoảng 75 chữ, 60 giây khoảng 170 chữ.

## Luật cứng (hook `kiem-tra-giong` tự kiểm)

- Không emoji. Không dấu gạch dài (em dash, en dash). Cần dấu nối thì dùng hyphen.
- Không dùng: "chữa khỏi", "trị liệu", "hết trầm cảm", "đổi đời", "giàu nhanh", "thành công nhanh", "ngay lập tức".
- Hạn chế "phải" kiểu ra lệnh. "Không phải là..." thì được.
- Caption 2 dòng, không link, không bán hàng.
- Link chỉ nằm ở comment ghim, luôn kèm chữ "link affiliate".
- Không hứa sách chữa bệnh hay thay đổi cuộc đời. Chỉ nói điều sách giúp Kioo nhìn ra.

## Sách

- Chủ lực: *Sức mạnh của tiềm thức* (Joseph Murphy), *Hiểu về trái tim*.
- Hỗ trợ theo nỗi đau: *Quẳng gánh lo đi và vui sống*, *Sức mạnh của hiện tại*, *Atomic Habits*, *Đời ngắn đừng ngủ dài*.
- Ý trong reel lấy từ `du-lieu/y-dat.csv`, là những ý Kioo đã tự đọc và ghi lại. Không bịa ý sách, không chép nguyên văn.
- Reel sách: phần "điều mình học được" luôn đánh dấu `[NHÁP - Kioo thay bằng điều thật]`.

Mẫu comment ghim:
> Ý trong reel hôm nay nhặt từ cuốn [tên sách]. Mình để link ở đây cho bạn nào cần (link affiliate: mình có hoa hồng nhỏ nếu bạn mua, giá không đổi). [link]

## Hình ảnh

- Dọc 9:16, 1080 x 1920. Chữ đặt ở 2/3 trên khung hình. Font serif mảnh, một cỡ chữ.
- Màu: xanh lá dịu, xanh dương nhạt, kem, đen mực. Film grain nhẹ, tông ấm hơi phai.
- Người phụ nữ quay lưng hoặc nhìn nghiêng, không thấy mặt.
- Đồ vật cũ: ấm trà, cuốn sổ, đèn vàng, cửa sổ gỗ, mưa, sách mở.
- Prompt cảnh viết tiếng Anh, 5 đến 8 giây, luôn kết bằng "vertical 9:16, no text, no logo".

## Thư mục

| Đường dẫn | Chứa gì |
|---|---|
| `lo/<năm>-W<tuần>/` | Lô reel từng tuần: `sang.md`, `trua.md`, `toi.md` và file CSV cho Canva |
| `du-lieu/y-dat.csv` | Ý đắt Kioo ghi từ sách |
| `du-lieu/theo-doi.csv` | Bảng theo dõi mọi reel đã đăng |
| `bao-cao/` | Báo cáo số liệu hàng tuần |
| `.claude/skills/lo-reel/vi-du/` | 14 reel đầu, bài mẫu chuẩn giọng |

## Cách làm việc

- `/lo-reel`: viết lô reel tuần.
- `/doc-so-lieu`: đọc số liệu cuối tuần.
- Viết xong luôn gọi agent `bien-tap-vien` duyệt trước khi đưa Kioo xem.
- Không tự đăng. Kioo duyệt từng reel.
- Câu trích dẫn: ghi nguồn, đánh dấu chỗ cần Kioo kiểm bản dịch.
