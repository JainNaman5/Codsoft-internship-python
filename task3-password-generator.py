import random
import string

def generate_password(length):
    """Generate a random password with specified length."""
    # All possible characters: letters, numbers, and symbols
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # Generate password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to run the password generator."""
    print("=== Password Generator ===")
    
    while True:
        # Get password length from user
        try:
            length = int(input("Enter password length: "))
            if length < 1:
                print("Length must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate and display password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")
    print(f"Length: {len(password)} characters")

if __name__ == "__main__":
    main()