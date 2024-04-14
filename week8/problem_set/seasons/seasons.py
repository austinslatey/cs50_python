from datetime import date
import inflect
import sys

inflect_engine = inflect.engine()


def main():
    try:
        date_of_birth_input = input("Enter your date of birth (YYYY-MM-DD): ")
        days_difference = date.today() - date.fromisoformat(date_of_birth_input)
        print(convert_days_to_words(days_difference.days))
    except ValueError:
        sys.exit("Invalid date format or date.")


def convert_days_to_words(days):
    minutes = days * 24 * 60
    return f"{inflect_engine.number_to_words(minutes, andword='').capitalize()} minutes"


if __name__ == "__main__":
    main()
