import re

def check_password_strength(password):
    score = 0
    feedback = []

   
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z).")

    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!,@,#,$, etc.).")

    # Display Strength
    print("\nPassword Analysis")
    print("-" * 30)

    if score == 5:
        print("✅ Strength: Very Strong")
    elif score == 4:
        print("🟢 Strength: Strong")
    elif score == 3:
        print("🟡 Strength: Moderate")
    elif score == 2:
        print("🟠 Strength: Weak")
    else:
        print("🔴 Strength: Very Weak")

    # Suggestions
    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(item)
    else:
        print("\n🎉 Excellent! Your password meets all security requirements.")


def main():
    print("=" * 40)
    print("     PASSWORD COMPLEXITY CHECKER")
    print("=" * 40)

    password = input("Enter your password: ")
    check_password_strength(password)


if __name__ == "__main__":
    main()