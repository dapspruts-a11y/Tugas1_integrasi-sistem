from fastapi import FastAPI, HTTPException #Digunakan untuk membuat aplikasi/API menggunakan framework FastAPI Dan gunakan untuk menangani exception atau error yang terjadi dalam aplikasi/API.
from pydantic import BaseModel #Digunakan untuk membuat struktur atau format data yang diterima oleh API.
from typing import Optional #Digunakan agar suatu field boleh memiliki nilai atau boleh kosong (None).

#Membuat instance FastAPI untuk membuat aplikasi/API
app = FastAPI(
    title="Tugas 1 Integrasi Sistem",
    description="API Data Mahasiswa",
    version="1.0.0"
)


# Membuat model data mahasiswa menggunakan Pydantic
class Mahasiswa(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    ipk: Optional[float] = None
    semester: Optional[int] = None
    hobi: Optional[str] = None


# Database sementara untuk menyimpan data mahasiswa
mahasiswa_db = {}


# POST - Menambahkan data mahasiswa
@app.post("/mahasiswa/{mahasiswa_id}")
def create_mahasiswa(mahasiswa_id: int, mahasiswa: Mahasiswa):
#Mengecek apakah data mahasiswa dengan ID yang sama sudah ada di database sementara. Jika sudah ada, maka akan mengembalikan HTTPException dengan status code 400 dan detail "Data mahasiswa sudah ada".
#Jika belum ada, maka data mahasiswa akan ditambahkan ke database sementara dan mengembalikan pesan sukses beserta ID dan data mahasiswa yang ditambahkan.
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

#Mengecek apakah data mahasiswa dengan ID yang diberikan ada di database sementara. Jika tidak ada, maka akan mengembalikan HTTPException dengan status code 404 dan detail "Data mahasiswa tidak ditemukan".
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
#Mengecek apakah data mahasiswa dengan ID yang diberikan ada di database sementara. Jika tidak ada, maka akan mengembalikan HTTPException dengan status code 404 dan detail "Data mahasiswa tidak ditemukan".
    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(
            status_code=404,
            detail="Data mahasiswa tidak ditemukan"
        )
#Jika data mahasiswa dengan ID yang diberikan ada di database sementara, 
#maka data mahasiswa tersebut akan dihapus dari database sementara dan mengembalikan pesan sukses beserta ID mahasiswa yang dihapus.
    del mahasiswa_db[mahasiswa_id]

    return {
        "message": "Data mahasiswa berhasil dihapus",
        "id": mahasiswa_id
    }