def check_input(input_string):
    # conver input to lowercase and remove spacing
    processed_input = input_string.replace(" ", "").lower()

    # if input matches target string return yes
    if processed_input == "fortytwo" or processed_input == "42" or processed_input == "forty-two":
        return "Yes"
    else:
        return "No"


# prompt the user for an answer
user_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
# run the test cases
output = check_input(user_answer)
print(output)
