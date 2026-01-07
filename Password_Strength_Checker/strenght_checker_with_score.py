def check_password_strength(password):
    score = 0
    issues = []

    special_characters = "!@#$%^&*()-+"

    if len(password) >= 8:
        score += 1
    else:
        issues.append("- Password must be at least 8 characters long")

    if any(c.isupper() for c in password):
        score += 1
    else:
        issues.append("- Add at least one uppercase letter")

    if any(c.islower() for c in password):
        score += 1
    else:
        issues.append("- Add at least one lowercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        issues.append("- Add at least one digit")

    if any(c in special_characters for c in password):
        score += 1
    else:
        issues.append("- Add at least one special character")

    return score, issues


password = input("Enter your password: ").strip()
score, issues = check_password_strength(password)

if score == 5:
    print("Strong password")
elif score >= 3:
    print("Medium password")
else:
    print("Weak password")

for issue in issues:
    print(issue)
