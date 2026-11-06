"""Các thao tác lưu trữ dữ liệu cho ứng dụng quản lý tủ sách."""

import sqlite3
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


_THU_MUC_DU_LIEU = (
    Path(sys.executable).resolve().parent
    if getattr(sys, "frozen", False)
    else Path(__file__).resolve().parent
)
TEN_FILE_CSDL = _THU_MUC_DU_LIEU / "tu_sach.db"


@contextmanager
def ket_noi_csdl() -> Iterator[sqlite3.Connection]:
    """Mở kết nối và luôn đóng kết nối sau khi hoàn tất thao tác."""
    ket_noi = sqlite3.connect(TEN_FILE_CSDL)
    try:
        with ket_noi:
            yield ket_noi
    finally:
        ket_noi.close()


def tao_bang_neu_chua_co() -> None:
    with ket_noi_csdl() as ket_noi:
        ket_noi.execute(
            """
            CREATE TABLE IF NOT EXISTS sach (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ten_sach TEXT NOT NULL,
                tac_gia TEXT NOT NULL,
                the_loai TEXT NOT NULL,
                da_doc INTEGER NOT NULL DEFAULT 0 CHECK (da_doc IN (0, 1))
            )
            """
        )


def them_sach(ten_sach: str, tac_gia: str, the_loai: str) -> int:
    with ket_noi_csdl() as ket_noi:
        con_tro = ket_noi.execute(
            """
            INSERT INTO sach (ten_sach, tac_gia, the_loai)
            VALUES (?, ?, ?)
            """,
            (ten_sach, tac_gia, the_loai),
        )
        return int(con_tro.lastrowid)


def lay_toan_bo_sach() -> list[tuple[int, str, str, str, int]]:
    with ket_noi_csdl() as ket_noi:
        return ket_noi.execute(
            """
            SELECT id, ten_sach, tac_gia, the_loai, da_doc
            FROM sach
            ORDER BY ten_sach COLLATE NOCASE, id
            """
        ).fetchall()


def xoa_sach(id_sach: int) -> bool:
    with ket_noi_csdl() as ket_noi:
        con_tro = ket_noi.execute("DELETE FROM sach WHERE id = ?", (id_sach,))
        return con_tro.rowcount > 0


def danh_dau_da_doc(id_sach: int) -> bool:
    with ket_noi_csdl() as ket_noi:
        con_tro = ket_noi.execute(
            "UPDATE sach SET da_doc = 1 WHERE id = ? AND da_doc = 0",
            (id_sach,),
        )
        return con_tro.rowcount > 0


def thong_ke_theo_the_loai() -> list[tuple[str, int]]:
    with ket_noi_csdl() as ket_noi:
        return ket_noi.execute(
            """
            SELECT the_loai, COUNT(*)
            FROM sach
            GROUP BY the_loai
            ORDER BY the_loai COLLATE NOCASE
            """
        ).fetchall()
