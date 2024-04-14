def convert_case(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

def main():
    camel_case = input("Enter a variable name in camelCase: ")
    snake_case = convert_case(camel_case)
    print("Snake case:", snake_case)


if __name__ == "__main__":
    main()