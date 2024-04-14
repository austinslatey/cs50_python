import sys

def count_lines(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:

            # Read all lines from the file
            lines = file.readlines()

            # Init a counter for lines of code
            count = 0

            # Iterate through each line in the file
            for line in lines:

                # Check if line is not blank and does not start with the comment char '#'
                if line.strip() and not line.strip().startswith('#'):

                    # Increment the lines of code count
                    count += 1

             # Return the total count of lines of code
            return count

    except FileNotFoundError:
        # Send error if specific file does not exist
        sys.exit("File does not exist")


def main():
    # If command-line arguments does not equal 2 exit program with message: Too few command line arguments
    if len(sys.argv) != 2:
        sys.exit("Too few command line arguments")

    # Extract the file name from the command-line arguments
    filename = sys.argv[1]

    # Check if the file does not have a .py extention
    if not filename.endswith('.py'):
        # Exit the program with message: Not a Python file
        sys.exit("Not a Python file")

    # Call the count_lines func to count lines of code in python file
    print(count_lines(filename))


if __name__ == "__main__":
    main()
