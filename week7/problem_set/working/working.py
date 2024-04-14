import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regex pattern to match the time format
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$'
    match = re.match(pattern, s, re.IGNORECASE)

    if not match:
        raise ValueError("Invalid time format")

    # Extract components from the matched groups
    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or 0)
    start_meridiem = match.group(3)
    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or 0)
    end_meridiem = match.group(6)

    # Handle special case for "12 AM" to "00:00"
    if start_hour == 12 and start_meridiem.upper() == "AM":
        start_hour = 0
    if end_hour == 12 and end_meridiem.upper() == "AM":
        end_hour = 0

    # Convert hours to 24-hour format
    if start_meridiem.upper() == "PM" and start_hour != 12:
        start_hour += 12
    if end_meridiem.upper() == "PM" and end_hour != 12:
        end_hour += 12

    # Check for invalid times
    if not (0 <= start_hour <= 23 and 0 <= end_hour <= 23 and 0 <= start_minute < 60 and 0 <= end_minute < 60):
        raise ValueError("Invalid time")

    # Format the output
    start_time = f"{start_hour:02}:{start_minute:02}"
    end_time = f"{end_hour:02}:{end_minute:02}"

    return f"{start_time} to {end_time}"

if __name__ == "__main__":
    main()
