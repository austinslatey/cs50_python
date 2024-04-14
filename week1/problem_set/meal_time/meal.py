def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


def main():
    user_time = input("Enter the time (24-hour format please - HH:MM):")
    converted_time = convert(user_time)

    if 7 <= converted_time < 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time < 19:
        print("dinner time")


if __name__ == "__main__":
    main()