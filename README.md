# Quán Nhỏ Cuối Ngõ

Bộ cấu hình Claude Code cho fanpage Quán Nhỏ Cuối Ngõ: 3 reel mỗi ngày, 21 reel mỗi tuần.

## Mỗi tuần làm gì

1. **Đọc sách, ghi ý đắt** vào `du-lieu/y-dat.csv` (3 đến 5 ý mỗi chương, ghi bằng lời của Kioo).
2. **Mở Claude Code với repo này**, gõ lần lượt:
   - `/lo-reel sang`
   - `/lo-reel trua`
   - `/lo-reel toi`

   Mỗi lệnh ra 7 reel, đã qua kiểm tra giọng và biên tập viên.
3. **Duyệt và sửa** các chỗ `[NHÁP]` và `[Kioo kiểm nguồn]`.
4. **Dựng trên Canva:** Bulk Create với file `lo/<tuần>/canva-<khung>.csv`.
5. **Thu giọng, tự quay** các reel ghi "Kioo tự quay", rồi lên lịch trên Meta Business Suite.
6. **Cuối tuần:** xuất số liệu Insights, gõ `/doc-so-lieu` và gửi kèm file.

## Có gì trong repo

| File | Làm gì |
|---|---|
| `CLAUDE.md` | Sổ tay quán: giọng, luật, nhịp đăng. Claude đọc mỗi lần làm việc. Muốn đổi luật thì sửa ở đây. |
| `.claude/skills/lo-reel/` | Lệnh `/lo-reel`, viết lô reel và xuất CSV cho Canva |
| `.claude/skills/doc-so-lieu/` | Lệnh `/doc-so-lieu`, đọc số liệu và gợi ý tuần sau |
| `.claude/agents/bien-tap-vien.md` | Biên tập viên, tự duyệt mỗi lô |
| `.claude/hooks/kiem-tra-giong.py` | Tự kiểm tra em dash, emoji, từ cấm, độ dài câu, link trong caption, câu mở trùng |
| `tai-lieu/` | Kế hoạch fanpage gốc |
| `du-lieu/` | Ý đắt và bảng theo dõi |
| `lo/` | Các lô reel theo tuần |
| `bao-cao/` | Báo cáo số liệu theo tuần |

## Tự kiểm tra một file

```
python3 .claude/hooks/kiem-tra-giong.py lo/2026-W44/sang.md
```

Muốn đổi luật độ dài câu: sửa các con số ở đầu file `.claude/hooks/kiem-tra-giong.py`.
