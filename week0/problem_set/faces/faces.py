# prompt the user for input
input = input("enter :) or :( for mood: ")

input = input.replace(":)", "🙂")

input = input.replace(":(", "🙁")

# output modified input
print(input)