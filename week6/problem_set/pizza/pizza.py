import sys
import os.path
import csv
from tabulate import tabulate

def print_pizza_table(csv_filename):
    # Check if the file exists
    if not os.path.exists(csv_filename):
        sys.exit("File not found in path")

    # Check if the file extension is CSV
    if not csv_filename.lower().endswith('.csv'):
        sys.exit("Not a CSV file extension")

    # Read the CSV file
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # Check if there are exactly 3 columns
    if len(rows[0]) != 3:
        sys.exit("Invalid CSV format")

    # Determine if the pizza type is Sicilian
    is_sicilian = csv_filename.lower().startswith("sicilian")

    # Format the table using tabulate
    headers = ["Sicilian Pizza" if is_sicilian else "Regular Pizza", "Small", "Large"]
    table = []

    for row in rows:
        table.append([row[headers[0]], row[headers[1]], row[headers[2]]])

    # Print the formatted table
    print(tabulate(table, headers=headers, tablefmt="grid"))

def main():
    # Check if the num of command-line arguments is correct
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    # Extract the CSV filename from the command-line arguments
    csv_filename = sys.argv[1]

    # Print the pizza table
    print_pizza_table(csv_filename)

if __name__ == "__main__":
    main()
