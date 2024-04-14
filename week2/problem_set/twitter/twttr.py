def twttr():
    # prompt user for string
    input_str = input("Please enter a string of your choice: ")
    modified_input = ""

    # whether its uppercase or lowercase
    # omit the vowels from the string
    for char in input_str:
        if char.lower() not in "aeiou":
            modified_input += char

    # output string
    print("Modified Text:", modified_input)
if __name__ == "__main__":
    twttr()