# prompt user to get input
input = input("Type something: ")

# split the input into two words
words = input.split()

# join the words with "..." in between
result = "...".join(words)

# Output the result
print(result)