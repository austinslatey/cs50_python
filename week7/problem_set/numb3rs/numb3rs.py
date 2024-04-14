import re
import sys


def main():
    ip_address = input("IPv4 Address: ")
    if validate(ip_address):
        print("True")
        sys.exit(0)
    else:
        print("False")
        sys.exit(1)


def validate(ip):
    pattern = r"^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.|$)){4}\b$"
    if re.match(pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
