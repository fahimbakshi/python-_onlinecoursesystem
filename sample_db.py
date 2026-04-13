import psycopg2

conn = psycopg2.connect(
    database="course_db",
    user="postgres",
    password="your password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()