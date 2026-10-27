import psycopg2

conn = psycopg2.connect(database = "sqluser", 
                        user = "sqluser", 
                        host= '192.168.58.138',
                        password = "sqlME1000",
                        port = 5432)

cur = conn.cursor()

# Insert a query in the line below
cur.execute("SELECT * FROM actresses.models;")
rows = cur.fetchall()

conn.commit()
conn.close()

for row in rows:
    print(row[1])

