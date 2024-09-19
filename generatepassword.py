import random
import string

def generate_password(length):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters into one set
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length of the password (or '0' to quit): "))
            if length == 0:
                print("Exiting the password generator. Goodbye!")
                break
            if length < 4:
                print("Please choose a length of at least 4 characters for a strong password.")
                continue

            password = generate_password(length)
            print(f"Generated Password: {password}\n")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
