"""
Task 1 — Thu thập văn bản pháp luật về ma tuý và các chất cấm.

Hướng dẫn:
    1. Tìm tối thiểu 3 văn bản pháp luật (PDF/DOCX) từ các nguồn chính thống.
    2. Tải về và lưu vào data/landing/legal/
    3. Đặt tên file rõ ràng, không dấu, có năm ban hành.

Gợi ý nguồn:
    - https://thuvienphapluat.vn
    - https://vanban.chinhphu.vn
    - https://luatvietnam.vn

Gợi ý văn bản:
    - Luật Phòng, chống ma tuý 2021 (73/2021/QH15)
    - Nghị định 105/2021/NĐ-CP
    - Bộ luật Hình sự 2015 (sửa đổi 2017) - Chương XX
    - Nghị định 57/2022/NĐ-CP về danh mục chất ma tuý
"""

from pathlib import Path
from urllib.request import Request, urlopen

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data" / "landing" / "legal"

DOCUMENTS = [
    {
        "url": "https://datafiles.chinhphu.vn/cpp/files/vbpq/2022/01/73luat.pdf",
        "filename": "luat_phong_chong_ma_tuy_2021_73_2021_QH14.pdf",
        "source_page": "https://vanban.chinhphu.vn/?docid=204940&pageid=27160",
    },
    {
        "url": "https://datafiles.chinhphu.vn/cpp/files/vbpq/2021/12/105.signed_02.pdf",
        "filename": "nghi_dinh_105_2021_ND_CP_huong_dan_luat_phong_chong_ma_tuy.pdf",
        "source_page": "https://vanban.chinhphu.vn/?docid=204678&pageid=27160",
    },
    {
        "url": "https://datafiles.chinhphu.vn/cpp/files/vbpq/2022/08/57-cp.signed.pdf",
        "filename": "nghi_dinh_57_2022_ND_CP_danh_muc_chat_ma_tuy_va_tien_chat.pdf",
        "source_page": "https://vanban.chinhphu.vn/?classid=1&docid=206454&pageid=27160&typegroupid=4",
    },
]


def setup_directory():
    """Tạo thư mục data/landing/legal/ nếu chưa có."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[OK] Thu muc da san sang: {DATA_DIR}")


# TODO: Tải file PDF/DOCX về DATA_DIR
# Có thể tải thủ công hoặc viết script download nếu có direct link.
#
# Ví dụ nếu có direct link:
#
# import requests
#
# def download_file(url: str, filename: str):
#     response = requests.get(url)
#     filepath = DATA_DIR / filename
#     filepath.write_bytes(response.content)
#     print(f"✓ Đã tải: {filepath}")
def download_file(url: str, filename: str) -> None:
    """Tai file PDF/DOCX tu direct link ve DATA_DIR."""
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    filepath = DATA_DIR / filename
    with urlopen(request, timeout=60) as response:
        content = response.read()
    filepath.write_bytes(content)
    print(f"[OK] Da tai: {filepath} ({len(content):,} bytes)")


if __name__ == "__main__":
    setup_directory()
    for document in DOCUMENTS:
        download_file(document["url"], document["filename"])
