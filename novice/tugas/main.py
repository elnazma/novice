from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="tugas",
        user="postgres",
        password="7mei2004"
    )
    curs = conn.cursor()
    if request.method == "POST":
        tanggal = request.form.get("tanggal")
        nama = request.form.get("nama")
        kelas = request.form.get("kelas")
        keterangan = request.form.get("keterangan")
        query = f"insert into absensi(tanggal, nama, kelas, keterangan) values('{tanggal}', '{nama}', '{kelas}', '{keterangan}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from absensi"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)  

if __name__ == "__main__":
    app.run()