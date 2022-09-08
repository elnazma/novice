import psycopg2
from flask import request, render_template

def index():
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="7mei2004")
    curs = conn.cursor()

    
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)
        conn.commit()

        print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()
    # data = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Ahad"]
    return render_template("index.html", context=data)