def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    if dollars is not None and percent is not None:
        tip = dollars * percent / 100
        print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # try to return the float dollar except when there is an invalid amout
    try:
        return float(d.replace("$", ""))
    except ValueError:
        print("Invalid input.. Please enter a valid dollar amount!")
        return None


def percent_to_float(p):
    # try to return float percentage except for err
    try:
        return float(p.strip("%"))
    except ValueError:
        print("Invalid input.. Please enter a valid percentage")
        return None


main()