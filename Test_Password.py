import re

def is_strong_password(password):
    # Check the length of the password
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', password):
        return False

    return True

# Input a password to test
password = input("Enter a password: ")

if is_strong_password(password):
    print("Password is strong.")
else:
    print("Password is weak.")
