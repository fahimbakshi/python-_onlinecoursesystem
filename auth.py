from db import cur, conn

# CREATE (Register)
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cur.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cur.fetchone():
        print("❌ User already exists")
        return

    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    print("✅ Registered successfully")

# READ (Login)
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()

    if user:
        print("✅ Login successful")
        return user[0]  # return user_id
    else:
        print("❌ Invalid credentials")
        return None

# UPDATE (Change password)
def update_password(user_id):
    new_pass = input("Enter new password: ")
    cur.execute("UPDATE users SET password=%s WHERE id=%s", (new_pass, user_id))
    conn.commit()
    print("✅ Password updated")

# DELETE (Delete account)
def delete_user(user_id):
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    print("🗑 Account deleted")