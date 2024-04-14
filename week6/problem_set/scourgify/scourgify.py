import sys
import csv
import os


def parse_name(name):
    # Split the name into first and last names
    last_name, first_name = name.strip('""').split(', ')
    return first_name, last_name


def scourgify(input_file, output_file):
    try:
        # Read the CSV file input
        with open(input_file, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

        # Prepare data for the output CSV file
        output_data = []
        for row in rows:
            first_name, last_name = parse_name(row['name'])
            output_data.append(
                {'first': first_name, 'last': last_name, 'house': row['house']})

        # Write to CSV file
        with open(output_file, 'w', newline='') as csv_file:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output_data)

        # Print output
        print(f"Output written to {output_file}")

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


def main():
    # Check if correct num of command-line args is passed
    if len(sys.argv) < 3:
        print("Too few command-line arguments", file=sys.stderr)
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    if len(sys.argv) == 3:
        output_file = sys.argv[2]
    else:
        output_file = "output.csv"

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Could not read {input_file}", file=sys.stderr)
        sys.exit(1)

    scourgify(input_file, output_file)


if __name__ == "__main__":
    main()
