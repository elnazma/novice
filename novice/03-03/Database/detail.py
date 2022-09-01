# try:
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="contoh",
    user="postgres",
    password="7mei2004")

curs = conn.cursor()
query=f"select * from siswa where umur=18"
curs.execute(query)
data = curs.fetchone()
if not data:
    print("gak ada")
else:
    print("nama:", data[0], "umur:", data[1])