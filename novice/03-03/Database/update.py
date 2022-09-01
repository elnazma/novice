try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="7mei2004")

    curs = conn.cursor()

    namaLama = "nazlita"

    namaBaru = "maulydia"
    umurBaru = 17
    query = f"update siswa set nama='{namaBaru}', umur={umurBaru} where nama='{namaLama}'"
    curs.execute(query)
    conn.commit()
    print("data berhasil di update")
except Exception as e:
    print(e)
