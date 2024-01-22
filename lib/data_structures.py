# First, define the create_spicy_food function
def create_spicy_food(spicy_foods, spicy_food):
    # Append the new spicy_food to the spicy_foods list
    spicy_foods.append(spicy_food)
    
    # Return the updated list
    return spicy_foods

# Define your spicy_foods list
spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

# Define the new_spicy_food you want to add
new_spicy_food = {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}

# Now call create_spicy_food after its definition
updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)

# Print the updated list to verify the addition
print(updated_spicy_foods)

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)





