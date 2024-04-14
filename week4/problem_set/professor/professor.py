from random import randint


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_int(level)
        correct_answer = x + y
        tries = 0

        while tries < 3:
            guess = get_guess(x, y)
            if guess == correct_answer:
                score += 1
                break
            else:
                tries += 1
                if tries < 3:
                    print("EEE")
                else:
                    print(f"The correct answer is: {correct_answer}")
                    break

    print(f"{score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            print("Please enter 1, 2, or 3.")


def generate_int(level):
    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
    elif level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    else:
        x = randint(100, 999)
        y = randint(100, 999)
    return x, y


def get_guess(x, y):
    while True:
        try:
            guess = int(input(f"{x} + {y} = "))
            return guess
        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    main()
