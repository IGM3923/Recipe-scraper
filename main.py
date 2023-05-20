import csv
import random


def user_choices(recipes):
    while (True):
        combined_list = []
        meal_list = choose_meal(recipes)
        cuisine_list = choose_cuisine(recipes)

        # randomize from choices
        combined_list = common_member(meal_list,cuisine_list)
        if combined_list:
            rand = random.choice(combined_list)
            print("You should have " + rand + "!")
            print("Click for recipe: " + recipes[rand]['url'])
        else:
            print("No meals found with that combination")

        is_retry = input("Would you like to try again?\n"
                         "(Y/N)\n"
                         ">>>").lower()
        if is_retry != "y": 
            print("Enjoy your meal!")
            break


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

def choose_cuisine(recipes):
    cuisine_list = []
    valid_choices = ["indian", "chinese", "italian", "other", "any"]
    cuisine_choice = input("What cuisine would you like?\n"
                             + str(valid_choices) + "\n" +
                            ">>>").lower()
    
    if cuisine_choice in valid_choices:
        if cuisine_choice == "any":
            return list(recipes.keys())
        for r in recipes:
            if recipes[r]['cuisine'] == cuisine_choice:
                cuisine_list.append(r)
    return cuisine_list

def common_member(a, b):
    result = [i for i in a if i in b]
    return result

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
    



