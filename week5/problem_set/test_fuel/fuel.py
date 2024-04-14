def main():
    # Prompt user for fuel fraction input
    fraction = input("Enter fuel fraction (in X/Y format: )")

    try:
        # Covert the fuel fraction to a percentage
        percentage = convert(fraction)

        # Get the gauge status based on the percentage
        status = gauge(percentage)

        # Display the gauge status
        print("Fuel gauge status:", status)

    except (ValueError, ZeroDivisionError) as e:
        print("Error:", e)


def convert(fraction):
    # Split the fraction into the numerator and denominator
    numerator_str, denominator_str = fraction.split('/')

    try:
        # Convert numerator and denominator to integers
        numerator = int(numerator_str)
        denominator = int(denominator_str)
    except ValueError:
        raise ValueError("Numerator and denominator must be integers")

    # Check if the denominator is 0
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    # Calculate the percentage
    percentage = (numerator / denominator) * 100

    # Round the percentage to the nearest integer
    percentage = round(percentage)

    # Check if the percentage is within the valid range
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100")

    return int(percentage)


def gauge(percentage):
    # Determine the gauge status based on the percentage
    if percentage == 0:
        return "0%"
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
