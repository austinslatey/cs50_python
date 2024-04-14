def main():
    names = read_names()
    bid_adieu(names)


def read_names():
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass
    return names


def bid_adieu(names):
    length = len(names)
    if length == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif length == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        farewell = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"
        print(farewell)

if __name__ == "__main__":
    main()
