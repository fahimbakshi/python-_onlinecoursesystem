from db import cur, conn

# READ courses
def show_courses():
    cur.execute("SELECT * FROM courses")
    for c in cur.fetchall():
        print(f"ID: {c[0]} | Course: {c[1]} | Duration: {c[2]} | Fee: ₹{c[3]}")

# CREATE enrollment
def enroll(user_id):
    show_courses()
    cid = int(input("Enter course ID: "))

    cur.execute("SELECT * FROM enrollments WHERE user_id=%s AND course_id=%s", (user_id, cid))
    if cur.fetchone():
        print("❌ Already enrolled")
        return

    cur.execute("INSERT INTO enrollments (user_id, course_id) VALUES (%s, %s)", (user_id, cid))
    conn.commit()
    print("✅ Enrolled")

# READ my courses
def my_courses(user_id):
    cur.execute("""
    SELECT courses.name FROM courses
    JOIN enrollments ON courses.id = enrollments.course_id
    WHERE enrollments.user_id=%s
    """, (user_id,))

    data = cur.fetchall()
    print("\nMy Courses:")
    for d in data:
        print("-", d[0])

# DELETE enrollment
def unenroll(user_id):
    cid = int(input("Enter course ID to remove: "))
    cur.execute("DELETE FROM enrollments WHERE user_id=%s AND course_id=%s", (user_id, cid))
    conn.commit()
    print("🗑 Removed from course")