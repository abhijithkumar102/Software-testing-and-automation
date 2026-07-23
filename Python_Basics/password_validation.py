password = input("Enter Password: ")

if 8 <= len(password) <= 16:
    print("Valid Password")
else:
    print("Invalid Password")