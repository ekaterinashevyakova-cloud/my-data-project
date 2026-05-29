import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="gtm_intelligence",
    user="postgres",
    password="1234",
    port="5432"
)

print("Connected successfully!")

conn.close()
