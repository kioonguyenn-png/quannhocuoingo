---
name: lo-reel
description: Viết lô reel tuần cho Quán Nhỏ Cuối Ngõ (21 reel, 3 khung sáng, trưa, tối) từ bảng ý đắt và số liệu tuần trước, xuất thêm CSV cho Canva Bulk Create. Dùng khi Kioo gõ /lo-reel hoặc nhờ viết reel tuần mới.
disable-model-invocation: true
argument-hint: "[sang|trua|toi|ca-tuan] [tuần, ví dụ 2026-W44]"
---

# Viết lô reel tuần

Đọc `CLAUDE.md` trước. Giọng chuẩn nằm trong `vi-du/lo-14-reel-dau.md`: học cách mở, nhịp kể, cách đóng. Riêng độ dài câu thì theo luật mới trong CLAUDE.md (vài câu trong bài mẫu dài hơn 25 chữ, đừng bắt chước chỗ đó).

## Đầu vào

- Tham số 1: khung giờ cần viết. `sang`, `trua`, `toi`, hoặc `ca-tuan`. Không có thì hỏi Kioo.
  - Nên viết từng khung một (7 reel mỗi lần) để giọng không mòn về cuối.
- Tham số 2: tuần, dạng `2026-W44`. Không có thì lấy tuần kế tiếp so với hôm nay.
- `du-lieu/y-dat.csv`: ý đắt Kioo đã ghi. Ý nào đã dùng (cột `da_dung`) thì ưu tiên ý chưa dùng.
- `bao-cao/` mới nhất, nếu có: dùng gợi ý hook và dạng nội dung đang hiệu quả.
- Mọi file trong `lo/` của 4 tuần gần nhất: để không lặp câu mở, câu trích, cảnh quay.

## Phân bổ một tuần

| Thứ | Sáng | Trưa | Tối |
|---|---|---|---|
| Hai | Động viên | Trích dẫn | Kể chuyện |
| Ba | Động viên | Trích dẫn | **Sách** |
| Tư | Động viên | Trích dẫn | Kể chuyện |
| Năm | Động viên | Trích dẫn | Kể chuyện |
| Sáu | Động viên | **Sách** | Kể chuyện |
| Bảy | Động viên | Trích dẫn | Kể chuyện |
| CN | Động viên | Trích dẫn | Kể chuyện |

Tổng: 7 động viên, 6 trích dẫn, 6 kể chuyện, 2 sách. Đánh dấu khoảng 2 reel mỗi khung (6 reel cả tuần) dùng clip Kioo tự quay, ưu tiên reel sách và reel kể chuyện.

## Độ dài

| Dạng | Giây | Chữ lời đọc |
|---|---|---|
| Trích dẫn | 25 đến 30 | 65 đến 90 |
| Động viên | 30 đến 40 | 75 đến 120 |
| Kể chuyện | 45 đến 60 | 115 đến 175 |
| Sách | 50 đến 60 | 125 đến 175 |

## Định dạng file

Ghi vào `lo/<tuần>/<khung>.md` (ví dụ `lo/2026-W44/sang.md`). Mỗi reel đúng khung này, hook kiểm tra dựa vào nó:

```
# Lô <tuần> · <Sáng|Trưa|Tối>

### Reel <thứ>-<khung> · <Loại> · khoảng <N> giây
**Câu mở đầu.** <câu hook, cũng là dòng chữ đầu trên màn hình>
**Lời đọc.** <toàn bộ lời đọc>
**Chữ trên màn hình.** <dòng 1> / <dòng 2> / <dòng 3>
**Caption.** <dòng 1> / <dòng 2>
**Comment ghim.** <theo mẫu trong CLAUDE.md, ghi đúng tên sách>
**Ý gốc.** <mã ý trong y-dat.csv, hoặc nguồn câu trích>
**Cảnh quay.** <mô tả tiếng Việt> · Nguồn: <AI/stock | Kioo tự quay>
**Prompt cảnh.** 1) ... 2) ... 3) ...
```

Ví dụ tiêu đề: `### Reel T2-sang · Động viên · khoảng 30 giây`.

- Reel nào cũng có comment ghim dẫn về đúng một cuốn sách hợp với nỗi đau trong reel.
- Reel sách: phần điều học được đánh dấu `[NHÁP - Kioo thay bằng điều thật]`.
- Câu trích: thêm `[Kioo kiểm nguồn]` sau tên tác giả.

## Xuất CSV cho Canva

Ghi `lo/<tuần>/canva-<khung>.csv`, UTF-8, mỗi reel một dòng:

```
ma,ngay,khung,loai,dong_1,dong_2,dong_3,nguon_clip
T2-sang,2026-10-26,Sáng,Động viên,"Hôm nay không cần xuất sắc.","Chỉ cần có mặt.","Thương mình một chút nhé.",AI
```

Dòng chữ trên màn hình tối đa 8 chữ một dòng, để vừa 2/3 trên khung hình.

## Sau khi viết

1. Hook `kiem-tra-giong` tự chạy. Có lỗi thì sửa đến khi hết lỗi.
2. Gọi agent `bien-tap-vien` duyệt file vừa viết. Áp dụng các đề xuất "Sửa", liệt kê các đề xuất "Cân nhắc" cho Kioo.
3. Thêm dòng cho mỗi reel vào `du-lieu/theo-doi.csv` (để trống các cột số liệu). Đánh dấu ý đã dùng trong `du-lieu/y-dat.csv`.
4. Báo lại Kioo ngắn gọn: số reel, reel nào cần tự quay, reel nào có chỗ `[NHÁP]` hay `[Kioo kiểm nguồn]`, và các đề xuất cân nhắc.
