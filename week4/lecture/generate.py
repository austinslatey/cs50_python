from random import choice, shuffle

coin =  choice(["heads","tails"])

print(coin, "\n-------")


cards = ["queen", "jack", "king"]
shuffle(cards)
for card in cards:
    print(card)
