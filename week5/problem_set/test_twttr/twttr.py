def main():
    input_str = input("Please enter a string of your choosing: ")
    modified_input = shorten(input_str)
    print("Modified Text:", modified_input)


def shorten(word):
    return ''.join(char for char in word if char.lower() not in "aeiou")


if __name__ == "__main__":
    main()
