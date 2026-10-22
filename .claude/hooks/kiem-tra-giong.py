#!/usr/bin/env python3
"""Kiểm tra giọng Quán Nhỏ Cuối Ngõ mỗi khi Claude viết file trong thư mục lo/.

Chạy tay: python3 .claude/hooks/kiem-tra-giong.py lo/2026-W44/sang.md
Lỗi cứng -> báo lại cho Claude tự sửa. Cảnh báo -> Claude cân nhắc, không bắt buộc sửa.
"""
import json
import os
import re
import sys

# Chỉnh luật ở đây
CAU_DAI_CANH_BAO = 15   # câu dài hơn mức này bị đếm
CAU_DAI_TOI_DA = 25     # câu dài hơn mức này là lỗi
TY_LE_CAU_DAI = 0.34    # quá 1/3 số câu dài hơn 15 chữ thì cảnh báo
CHU_MOI_GIAY = (2.0, 3.2)
TU_CAM = ["chữa khỏi", "trị liệu", "hết trầm cảm", "đổi đời", "giàu nhanh",
          "thành công nhanh", "ngay lập tức"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\uFE0F]")


def doc_truong(than, ten):
    m = re.search(r"\*\*" + ten + r"\.\*\*\s*(.+)", than)
    return m.group(1).strip() if m else ""


def tach_cau(van):
    return [c.strip() for c in re.split(r"[.?!]+", van) if c.strip()]


def kiem_tra(duong_dan):
    van = open(duong_dan, encoding="utf-8").read()
    loi, canh_bao = [], []

    if "\u2014" in van or "\u2013" in van:
        loi.append("Có dấu gạch dài (em dash hoặc en dash). Thay bằng dấu phẩy, dấu chấm hoặc hyphen.")
    if EMOJI.search(van):
        loi.append("Có emoji.")
    thap = van.lower()
    for tu in TU_CAM:
        if tu in thap:
            loi.append(f'Có từ cấm "{tu}".')

    phan = re.split(r"^### Reel ", van, flags=re.M)
    for khoi in phan[1:]:
        dong_dau = khoi.splitlines()[0]
        ten = "Reel " + dong_dau.split("·")[0].strip()
        m = re.search(r"(\d+)\s*giây", dong_dau)
        giay = int(m.group(1)) if m else None

        loi_doc = doc_truong(khoi, "Lời đọc")
        if not loi_doc:
            loi.append(f"{ten}: thiếu phần Lời đọc.")
            continue
        so_chu = len(loi_doc.split())
        if giay:
            toc_do = so_chu / giay
            if not CHU_MOI_GIAY[0] <= toc_do <= CHU_MOI_GIAY[1]:
                loi.append(f"{ten}: {so_chu} chữ cho {giay} giây ({toc_do:.1f} chữ/giây). "
                           f"Cần {int(giay*CHU_MOI_GIAY[0])} đến {int(giay*CHU_MOI_GIAY[1])} chữ.")

        cau = tach_cau(loi_doc)
        qua_dai = [c for c in cau if len(c.split()) > CAU_DAI_TOI_DA]
        for c in qua_dai:
            loi.append(f'{ten}: câu {len(c.split())} chữ, quá {CAU_DAI_TOI_DA}: "{c[:60]}..."')
        dai = [c for c in cau if len(c.split()) > CAU_DAI_CANH_BAO]
        if cau and len(dai) / len(cau) > TY_LE_CAU_DAI:
            canh_bao.append(f"{ten}: {len(dai)}/{len(cau)} câu dài hơn {CAU_DAI_CANH_BAO} chữ, nên tách bớt.")

        for c in re.findall(r"[^.?!]*\bphải\b[^.?!]*", loi_doc, flags=re.I):
            if not re.search(r"không phải|phải không", c, flags=re.I):
                canh_bao.append(f'{ten}: "phải" có thể nghe như ra lệnh: "{c.strip()[:60]}"')

        caption = doc_truong(khoi, "Caption")
        if re.search(r"https?://|www\.|\.com|shope|tiktok\.|lazada", caption, flags=re.I):
            loi.append(f"{ten}: caption có link. Link chỉ để ở comment ghim.")

        comment = doc_truong(khoi, "Comment ghim")
        if comment and ("link" in comment.lower() or "[link]" in comment) \
                and "link affiliate" not in comment.lower():
            loi.append(f'{ten}: comment ghim có link nhưng thiếu chữ "link affiliate".')

    # Câu mở trùng với các lô khác
    mo_hien_tai = {c.strip().lower() for c in re.findall(r"\*\*Câu mở đầu\.\*\*\s*(.+)", van)}
    goc = re.split(r"[/\\]lo[/\\]", os.path.abspath(duong_dan))[0]
    thu_muc_lo = os.path.join(goc, "lo")
    if mo_hien_tai and os.path.isdir(thu_muc_lo):
        for thu_muc, _, cac_file in os.walk(thu_muc_lo):
            for f in cac_file:
                p = os.path.join(thu_muc, f)
                if not f.endswith(".md") or os.path.abspath(p) == os.path.abspath(duong_dan):
                    continue
                cu = {c.strip().lower() for c in re.findall(r"\*\*Câu mở đầu\.\*\*\s*(.+)",
                                                            open(p, encoding="utf-8").read())}
                for c in mo_hien_tai & cu:
                    loi.append(f'Câu mở trùng với {os.path.relpath(p, goc)}: "{c[:60]}"')
    return loi, canh_bao


def main():
    if len(sys.argv) > 1:  # chạy tay
        tong = 0
        for p in sys.argv[1:]:
            loi, cb = kiem_tra(p)
            print(f"== {p}: {len(loi)} lỗi, {len(cb)} cảnh báo")
            for x in loi:
                print("  LỖI     " + x)
            for x in cb:
                print("  CẢNH BÁO " + x)
            tong += len(loi)
        sys.exit(1 if tong else 0)

    du_lieu = json.load(sys.stdin)
    p = (du_lieu.get("tool_input") or {}).get("file_path", "")
    if not p.endswith(".md") or not re.search(r"[/\\]lo[/\\]", p) or not os.path.exists(p):
        sys.exit(0)
    loi, cb = kiem_tra(p)
    if loi:
        thong_bao = "Kiểm tra giọng: file " + os.path.basename(p) + " chưa đạt. Sửa các lỗi sau:\n- " \
                    + "\n- ".join(loi)
        if cb:
            thong_bao += "\nCảnh báo (cân nhắc, không bắt buộc):\n- " + "\n- ".join(cb)
        print(thong_bao, file=sys.stderr)
        sys.exit(2)
    if cb:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": "Kiểm tra giọng: không có lỗi. Cảnh báo để cân nhắc:\n- " + "\n- ".join(cb),
        }}, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
