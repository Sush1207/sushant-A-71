import random
import string

def generate_strong_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_multiple_strong_passwords(num_passwords, length):
    passwords = [generate_strong_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    print("Generating strong, secure passwords:")
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    generated_passwords = generate_multiple_strong_passwords(num_passwords, password_length)

    print("\nGenerated Passwords:")
    for password in generated_passwords:
        print(password)
