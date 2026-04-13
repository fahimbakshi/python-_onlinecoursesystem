from auth import register, login, update_password, delete_user
from courses import enroll, my_courses, unenroll

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        register()

    elif ch == "2":
        user_id = login()

        if user_id:
            while True:
                print("\n1. Enroll")
                print("2. My Courses")
                print("3. Unenroll")
                print("4. Update Password")
                print("5. Delete Account")
                print("6. Logout")

                c = input("Enter choice: ")

                if c == "1":
                    enroll(user_id)
                elif c == "2":
                    my_courses(user_id)
                elif c == "3":
                    unenroll(user_id)
                elif c == "4":
                    update_password(user_id)
                elif c == "5":
                    delete_user(user_id)
                    break
                elif c == "6":
                    break

    elif ch == "3":
        break