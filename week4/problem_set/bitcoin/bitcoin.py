from sys import exit, argv
from requests import get, RequestException


def main():
    # Check if the number of Bitcoins is provided as a command-line argument
    if len(argv) != 2:
        exit("Missing command-line argument")

    # Try to convert the command line argument to a float
    try:
        btc = float(argv[1])
    except ValueError:
        exit("Command-line argument is not a number")

    # Query the CoinDesk Bitcoin Price Index API
    try:
        response = get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Exception for HTTP errors
        response.raise_for_status()

        btc_data = response.json()
        btc_per_usd = btc_data["bpi"]["USD"]["rate_float"]

    except RequestException as e:
        exit(f"Error retrieving BTC price: {e}")

    # Calculate total cost of num of btc
    total_usd = btc * btc_per_usd

    # output cost of btc
    print(f"${total_usd:,.4f}")


if __name__ == "__main__":
    main()
