def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    if not s[-1].isdigit():
        return False

    if s[-1] == '0':
        return False

    if any(char.isdigit() for char in s[2:-1]):
        return False

    return True



main()
