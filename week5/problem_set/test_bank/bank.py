def main():
    # prompt user for greeting
    user_greeting = input("Enter a greeting: ")
    payment = value(user_greeting)
    print("Bank payment: ", payment)

def value(greeting):
    # ignore any leading whitespace in greeting and treat input case insensitively
    greeting = greeting.strip().lower()

     # if "hello" output $0
    if greeting.startswith("hello"):
        return 0

    # if greeting starts with "h" but not hello.. output $20
    if greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
