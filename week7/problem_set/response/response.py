# pip install validator-collection
# pip install validators
from validators import email as validate_email

def main():
    # Ask user for email
    email = input("What's your email? ").strip()

    # Validate email using validators function to check email
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
