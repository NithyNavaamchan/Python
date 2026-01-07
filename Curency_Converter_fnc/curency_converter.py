def check_password_strength(password):
    import re

    is_upper = False
    is_lower = False
    is_digit = False
    is_special = False

    special_characters = re.compile(r'[@_!#$%^&*()<>?/\\|}{~:]')


    for char in password:
        if char.isupper():
            is_upper = True
        elif char.islower():
            is_lower = True
        elif char.isdigit():
            is_digit = True
        elif char in special_characters.pattern:
            is_special = True

    length = len(password)

    if length >= 8 and is_upper and is_lower and is_digit and is_special:
        return "Strong password"
    else:
        weaknesses = []
        if length < 8:
            weaknesses.append("- Password must be at least 8 characters long.")
        if not is_upper:
            weaknesses.append("- Password must contain at least one uppercase letter.")
        if not is_lower:
            weaknesses.append("- Password must contain at least one lowercase letter.")
        if not is_digit:
            weaknesses.append("- Password must contain at least one digit.")
        if not is_special:
            weaknesses.append("- Password must contain at least one special character (@_!#$%^&*()<>?/\\|}{~:).")
        
        return "Weak password\n" + "\n".join(weaknesses)
    
"""
def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = set("@_!#$%^&*()<>?/\\|}{~:")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

        if has_upper and has_lower and has_digit and has_special:
            break

    length = len(password)

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong password"
    else:
        issues = []

        if length < 8:
            issues.append("- At least 8 characters required")
        if not has_upper:
            issues.append("- Add an uppercase letter")
        if not has_lower:
            issues.append("- Add a lowercase letter")
        if not has_digit:
            issues.append("- Add a digit")
        if not has_special:
            issues.append("- Add a special character")

        return "Weak password\n" + "\n".join(issues)
"""