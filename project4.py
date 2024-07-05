import random
import string

def generate_password(length):
    if length < 4:  # Ensure the length is enough to include all types of characters
        raise ValueError("Password length should be at least 4 characters.")
    
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    
    password += random.choices(all_chars, k=length-4)
    random.shuffle(password)
    
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the password length: "))
        number = int(input("Enter the number of passwords to generate: "))
        
        for _ in range(number):
            print(generate_password(length))
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
