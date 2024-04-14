from sys import argv, exit

if len(argv) < 2:
    exit("Too few arguments")
elif len(argv) > 2:
    exit("Too many arguments")

print("hello, my name is", argv[1])
