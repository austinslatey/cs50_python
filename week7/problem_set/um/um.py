import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Match the word "um" as a whole word, using \b to match word boundaries.
    pattern = r"\bum\b"

    # Find all non-overlapping occurrences of the pattern in the input text 's'
    matches = re.findall(pattern, s, re.IGNORECASE)

    # Return found matches
    return len(matches)




if __name__ == "__main__":
    main()
