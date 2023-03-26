minimum_password_length = 4


def main():
    password = get_password(minimum_password_length)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Enter a password: ")

    if len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long.")
        return get_password(minimum_length)
    else:
        return password


def print_asterisks(password):
    print("*" * len(password))


main()
