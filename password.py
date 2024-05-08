def is_valid_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    return True

while True:
    try:
        password = input("Enter your password: ")
        is_valid_password(password)
        print("Password is valid.")
        break
    except ValueError as error:
        print(error)
