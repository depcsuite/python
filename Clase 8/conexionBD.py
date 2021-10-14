import psycopg2
conn = psycopg2.connect(
   database="proyectocurso", user='postgres', password='pass', host='127.0.0.1', port= '5432'
)
cur = conn.cursor()
cur.execute("select current_database()")
result = cur.fetchone()
print(result)
conn.close()