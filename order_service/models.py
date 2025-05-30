from database import get_db_connection

def simpan_pesanan(nama_pemesan, id_obat, jumlah, kategori):
    status = "Normal"
    if kategori.lower() == 'merah' and int(jumlah) > 3:
        status = "Anomali"
    
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO pesanan (nama_pemesan, id_obat, jumlah, kategori, status) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nama_pemesan, id_obat, jumlah, kategori, status))
    conn.commit()
    conn.close()

def get_all_pesanan():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pesanan")
    results = cursor.fetchall()
    conn.close()
    return results
