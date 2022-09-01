try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="7mei2004")

    curs = conn.cursor()

    nama = "maulydia"

    query = f"delete from siswa where nama='{nama}'"
    curs.execute(query)
    conn.commit()
    print("data berhasil di hapus")
except Exception as e:
    print(e)
