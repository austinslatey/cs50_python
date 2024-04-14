names = []

for _ in range(3):
    names.append(input("What's your name? "))

# Sort names
sorted_names = sorted(names)

# Write sorted names to file
with open("names.txt", "w") as file:
    for name in sorted_names:
        file.write(f"{name}\n")

# Read names from file and greet each person
with open("names.txt") as file:
    for line in file:
        name = line.strip()
        print("hello", name)
