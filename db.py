import psycopg2

conn = psycopg2.connect(
    database="course_db",
    user="postgres",
    password="fahim.123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()