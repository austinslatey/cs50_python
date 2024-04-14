from random import randint


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError
            return level
        except ValueError:
            print("Please enter a positive integer.")


def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                raise ValueError
            return guess
        except ValueError:
            print("Please enter a positive integer")


def main():
    level = get_level()
    target_number = randint(1, level)

    while True:
        guess = get_guess()

        if guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
