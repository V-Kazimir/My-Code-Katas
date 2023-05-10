import re

def check_password_strength(password):

    # Minimum password length
    if len(password) < 12:
        return "Password should be at least 12 characters long, but 14 or more is better."

    # Check for uppercase, lowercase, digits, and special characters
    if not re.search(r"[A-Z]", password):
        return "Password should contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password should contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return "Password should contain at least one digit."
    if not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~\"]", password):
        return "Password should contain at least one special character."

    # Password meets all criteria
    return "Password is suitable."

if __name__ == '__main__':
    password = input("Enter password to check: ")
    strength = check_password_strength(password)
    print(strength)
