# try:
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="contoh",
    user="postgres",
    password="7mei2004")

# except Exceptionas e:
#     print(e)

curs = conn.cursor()
query=f"select * from siswa"
curs.execute(query)
data = curs.fetchall()

for d in data:
    print("nama:", d[0], "umur:", d[1])