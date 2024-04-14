months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def validate_date(date_str):
    parts = date_str.replace('-', '/').split('/')

    if len(parts) == 3:
        try:
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
            if month < 1 or month > 12 or day < 1 or day > 31 or year < 1:
                return False
            return True
        except ValueError:
            return False

    parts = date_str.split()
    if len(parts) == 3:
        month_name = parts[0]
        day = ''.join(filter(str.isdigit, parts[1]))
        year = parts[2]
        if month_name in months.keys():
            if int(day) < 1 or int(day) > 31:
                return False
            # Check if the date string includes a comma
            if ',' not in date_str:
                return False
            return True

    return False


def format_date(date_str):
    parts = date_str.replace('-', '/').split('/')
    if len(parts) == 3:
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
        return f"{year:04d}-{month:02d}-{day:02d}"
    else:
        parts = date_str.split()
        month = months[parts[0]]
        # Convert day to integer
        day = int(''.join(filter(str.isdigit, parts[1])))
        year = int(parts[2])
        return f"{year:04d}-{month:02d}-{day:02d}"


def main():
    while True:
        user_input = input("Enter a date (in month-day-year or Month Day, Year format): ").strip()
        if validate_date(user_input):
            formatted_date = format_date(user_input)
            print(formatted_date)
            break
        else:
            print("Invalid date. Please enter a valid date")


if __name__ == "__main__":
    main()
