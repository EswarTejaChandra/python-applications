import random
import string


def generate_password(length=12):
    # Define characters to use in the password
    letters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation
    space_bar = ' '
    all_chars = letters + numbers + special_chars + space_bar

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    # Generate a password with default length 12
    password = generate_password()
    print("Generated Password:", password)
