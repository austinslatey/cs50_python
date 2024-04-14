fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "grapes": 52,
    "Oranges": 62,
    "Peaches": 59,
    "pear": 100,
    "Pineapple": 83,
    "Strawberries": 32,
    "Watermelon": 46,
    "Blueberries": 57,
    "Cantaloupe": 54,
    "sweet cherries": 100,
    "Cranberries": 46,
    "Honeydew": 64,
    "kiwifruit": 90,
    "Mangoes": 135,
    "Nectarines": 63,
    "Plums": 46,
    "Raspberries": 64,
    "Tangerines": 47
}

fruit_prompt = input("Fruit: ")

for key in fruit_calories:
    if key == fruit_prompt.lower():
        print("Calories:", fruit_calories[key])
