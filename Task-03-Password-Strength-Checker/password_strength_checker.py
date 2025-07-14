import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (minimum 8 characters)": length_error,
        "Missing lowercase letter": lowercase_error,
        "Missing uppercase letter": uppercase_error,
        "Missing number": digit_error,
        "Missing special character": special_char_error
    }

    # Feedback
    failed = [msg for msg, err in errors.items() if err]
    
    if not failed:
        return "✅ Strong password!"
    elif len(failed) <= 2:
        return "⚠️ Medium strength. Suggestions:\n- " + "\n- ".join(failed)
    else:
        return "❌ Weak password. You should:\n- " + "\n- ".join(failed)

# Main program
print("🔐 Password Strength Checker")
user_password = input("Enter your password: ")

feedback = check_password_strength(user_password)
print("\nPassword Feedback:")
print(feedback)
