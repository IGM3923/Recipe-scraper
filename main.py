import csv
import random

def choose_meal(recipes):
    meal_list = []
    valid_choices = ["breakfast", "lunch/dinner", "dessert", "any"]
    meal_choice = input("What meal would you like? \n"
                        + str(valid_choices) + "\n" +
                        ">>>").lower()
    if meal_choice in valid_choices:
        if meal_choice == "any":
            return list(recipes.keys())
        else:
            for r in recipes:
                if recipes[r]['meal'] == meal_choice:
                    meal_list.append(r)
    return meal_list


def common_member(a, b):
    result = [i for i in a if i in b]
    return result

def user_choices(recipes):
    is_empty = False
    while (True):
        meal_list = choose_meal(recipes)

        # randomize from choice
        rand = random.choice(meal_list)
        print("You should have " + rand + "!")
        print("Click for recipe: " + recipes[rand]['url'])
       
        is_retry = input("Would you like to try again?\n"
                         "['Y'/'N']\n"
                         ">>>").lower()
        if is_retry != "y": 
            break

    if not is_empty:
        print("Enjoy your meal!")

if __name__ == "__main__":
    filename = "recipes.csv"
    with open(filename, 'r') as data:
        recipes = {}
        for line in csv.DictReader(data):
            name = line.pop("name")
            if name in recipes:
                pass
            recipes[name] = line
    user_choices(recipes)


    



