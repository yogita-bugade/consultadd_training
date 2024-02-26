'''Create a login page backend to ask users to enter the username
and password. Make sure to ask for a Re-Type Password and if the
password is incorrect give a chance to enter it again but it should
not be more than 3 times.'''
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    retype_password = input("Re-Type Password: ")
    if password != retype_password:
        print("Password doesn't match.Please re-enter.")
        for _ in range(2):
            retype_password = input("Re-Type Password:")
            if password == retype_password:
                break
        else:
            print("Password mismatch.Login failed")
            return
    print("Login successful!")

def main():
    for _ in range(3):
        login()
        break

if __name__ == "__main__":
    main()