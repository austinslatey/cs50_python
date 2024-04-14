from sys import argv, exit
from pyfiglet import FigletFont, figlet_format
from random import choice


def main():
    # parse command-line arguments
    if len(argv) == 1:
        font = choice(FigletFont.getFonts())
    elif len(argv) == 3 and (argv[1] == '-f' or argv[1] == '--font'):
        font = argv[2]
        if font not in FigletFont.getFonts():
            exit("Invalid usage: Font not found")
    else:
        exit("Invalid usage")

    # promt user for input
    text = input("Enter text: ")

    # Generate ASCII
    ascii_art = figlet_format(text, font=font)

    print(ascii_art)


if __name__ == "__main__":
    main()
