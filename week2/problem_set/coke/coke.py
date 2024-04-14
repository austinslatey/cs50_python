def coke_machine():
    total_amount = 0

    while total_amount < 50:
        coin = int(input("Insert a coin (5, 10, or 25 cents): "))

        if coin == 5 or coin == 10 or coin == 25:
            total_amount += coin
            if total_amount < 50:
                print("Amount Due:", 50 - total_amount)
        else:
            print("Invalid Coin")
            print("Amount Due:", 50 - total_amount)

    change = total_amount - 50
    print("Change Owed:", change)

if __name__ == "__main__":
    coke_machine()
