import psycopg2
conn = psycopg2.connect(
   database="proyectocurso", user='postgres', password='vordank', host='127.0.0.1', port= '5432'
)
cur = conn.cursor()
#cur.execute("select current_database()")
#cur.execute("select * from producto")
result = cur.fetchall()
print(result)
conn.close()