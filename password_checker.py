def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    digit_error = not any(char.isdigit() for char in password)
    special_error = not any(char in "!@#$%^&*()-_+=<>?/{}[]|" for char in password)

    errors = [
        length_error,
        uppercase_error,
        lowercase_error,
        digit_error,
        special_error
    ]

    if sum(errors) == 0:
        return "Strong Password ✅"
    elif sum(errors) <= 2:
        return "Medium Password ⚠️"
    else:
        return "Weak Password ❌"


if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print(result)
