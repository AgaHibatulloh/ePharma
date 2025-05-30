from database import get_db_connection

def tambah_kategori(nama_kategori):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO kategori_obat (nama_kategori) VALUES (%s)"
    cursor.execute(query, (nama_kategori,))
    conn.commit()
    conn.close()

def tambah_obat(nama, stok, kategori_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO obat (nama_obat, stok, kategori_id) VALUES (%s, %s, %s)"
    cursor.execute(query, (nama, stok, kategori_id))
    conn.commit()
    conn.close()

def get_all_obat():
    """
    Mengambil daftar semua obat dari database
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT o.id, o.nama_obat, o.stok, k.nama_kategori 
        FROM obat o JOIN kategori_obat k ON o.kategori_id = k.id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def get_kategori():
    """
    Mengambil daftar kategori obat
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM kategori_obat")
    results = cursor.fetchall()
    conn.close()
    return results

def get_obat_by_id(id):
    """
    Mengambil data obat berdasarkan ID
    """
    # Implementasi contoh
    obat = {"id": id, "nama_obat": "Paracetamol", "stok": 100, "kategori_id": 1}
    return obat

def update_obat(id, nama_obat, stok, kategori_id):
    """
    Memperbarui data obat
    """
    # Implementasi contoh
    print(f"Obat {id} diperbarui: {nama_obat}, stok: {stok}, kategori: {kategori_id}")
    return True

def delete_obat(id):
    """
    Menghapus obat dari database
    """
    # Implementasi contoh
    print(f"Obat {id} dihapus")
    return True
