password = (input("Enter your password: ")).strip()

length = len(password)
has_upperr = False
has_lowerr = False
has_digit = False
has_specialr = False

special_characters = "!@#$%^&*()-+"

for char in password:
    if char.isupper():
        has_upperr = True
    elif char.islower():
        has_lowerr = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_specialr = True

if length >= 8 and has_upperr and has_lowerr and has_digit and has_specialr:
    print("Strong password")

else:
    print("Weak password")


    if length < 8:
        print("- Password must be at least 8 characters long.")
    if not has_upperr:
        print("- Password must contain at least one uppercase letter.")
    if not has_lowerr:
        print("- Password must contain at least one lowercase letter.")
    if not has_digit:
        print("- Password must contain at least one digit.")
    if not has_specialr:
        print("- Password must contain at least one special character (!@#$%^&*()-+).")
    