from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Tugas 1 Integrasi Sistem",
    description="API Data Mahasiswa",
    version="1.0.0"
)


# Model Data
class Mahasiswa(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    ipk: Optional[float] = None
    semester: Optional[int] = None
    hobi: Optional[str] = None


# Database sementara
mahasiswa_db = {}


# POST - Menambahkan data mahasiswa
@app.post("/mahasiswa/{mahasiswa_id}")
def create_mahasiswa(mahasiswa_id: int, mahasiswa: Mahasiswa):

    if mahasiswa_id in mahasiswa_db:
        raise HTTPException(
            status_code=400,
            detail="Data mahasiswa sudah ada"
        )

    mahasiswa_db[mahasiswa_id] = mahasiswa

    return {
        "message": "Data mahasiswa berhasil ditambahkan",
        "id": mahasiswa_id,
        "data": mahasiswa
    }


# GET - Mengambil data mahasiswa
@app.get("/mahasiswa/{mahasiswa_id}")
def get_mahasiswa(mahasiswa_id: int):

    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="Data mahasiswa tidak ditemukan"
        )

    return {
        "id": mahasiswa_id,
        "data": mahasiswa_db[mahasiswa_id]
    }


# PUT - Mengubah data mahasiswa
@app.put("/mahasiswa/{mahasiswa_id}")
def update_mahasiswa(
    mahasiswa_id: int,
    mahasiswa: Mahasiswa
):

    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="Data mahasiswa tidak ditemukan"
        )

    mahasiswa_db[mahasiswa_id] = mahasiswa

    return {
        "message": "Data mahasiswa berhasil diperbarui",
        "id": mahasiswa_id,
        "data": mahasiswa
    }


# DELETE - Menghapus data mahasiswa
@app.delete("/mahasiswa/{mahasiswa_id}")
def delete_mahasiswa(mahasiswa_id: int):

    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="Data mahasiswa tidak ditemukan"
        )

    del mahasiswa_db[mahasiswa_id]

    return {
        "message": "Data mahasiswa berhasil dihapus",
        "id": mahasiswa_id
    }