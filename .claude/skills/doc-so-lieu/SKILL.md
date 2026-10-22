---
name: doc-so-lieu
description: Đọc số liệu reel tuần qua của Quán Nhỏ Cuối Ngõ, cập nhật bảng theo dõi, so sánh khung giờ, dạng nội dung, sách, và gợi ý hook cho tuần sau. Dùng khi Kioo gõ /doc-so-lieu hoặc gửi file số liệu Insights.
disable-model-invocation: true
argument-hint: "[file số liệu .csv/.xlsx, hoặc dán bảng]"
---

# Đọc số liệu tuần

## Đầu vào

- File Kioo xuất từ Meta Business Suite (Insights, mục Nội dung), hoặc bảng dán trực tiếp.
- `du-lieu/theo-doi.csv`: danh sách reel đã đăng, ghép với số liệu theo cột `ma` hoặc theo ngày và khung giờ.
- Số lượt bấm link lấy từ trang thống kê link rút gọn hoặc trang affiliate, nếu Kioo gửi kèm.

Không đủ dữ liệu thì nói rõ thiếu gì, không đoán số.

## Việc cần làm

1. Điền số liệu vào `du-lieu/theo-doi.csv`: `luot_xem`, `giu_chan`, `luu`, `chia_se`, `bam_link`.
2. Viết `bao-cao/<tuần>.md`, gồm:
   - **3 dòng tóm tắt** ở đầu: tuần này tốt ở đâu, yếu ở đâu, đổi gì tuần sau.
   - **Theo khung giờ:** lượt xem và giữ chân trung bình của sáng, trưa, tối.
   - **Theo dạng:** động viên, trích dẫn, kể chuyện, sách.
   - **Top 3 và đáy 3 reel** theo giữ chân, kèm câu mở. Giải thích ngắn vì sao câu mở đó giữ hoặc mất người xem.
   - **Theo sách:** lượt bấm link của từng cuốn.
   - **So với KPI** trong `tai-lieu/ke-hoach-fanpage.md`, tính theo nhịp 3 reel/ngày (ngày 30 là 90 reel).
   - **5 câu mở mới** cho tuần sau, cùng kiểu với các câu đang giữ chân tốt, không trùng câu đã dùng.
   - **Gợi ý ghép sách:** reel dạng nào nên dẫn về cuốn nào.
3. Sau 2 tuần đầu: chốt khung giờ đăng tốt nhất trong ngày, ghi vào báo cáo.

Chỉ kết luận khi mỗi nhóm có ít nhất 5 reel. Ít hơn thì ghi "chưa đủ số để kết luận".
