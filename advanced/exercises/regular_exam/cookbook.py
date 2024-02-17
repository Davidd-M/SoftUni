def cookbook(*args):
    cuisines_dict = {}
    for arg in args:
        recipe_name = arg[0]
        cuisine = arg[1]
        list_ingredients = arg[2]
        if cuisine not in cuisines_dict.keys():
            cuisines_dict[cuisine] = {recipe_name: list_ingredients}
        else:
            cuisines_dict[cuisine].update({recipe_name: list_ingredients})
    cuisines_dict = dict(sorted(cuisines_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for cuisine, recipes in cuisines_dict.items():
        cuisines_dict[cuisine] = dict(sorted(recipes.items()))
    formatted_output = ""
    for cuisine, recipes in cuisines_dict.items():
        formatted_output += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        for recipe, ingredients in recipes.items():
            formatted_output += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"
    return formatted_output


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))

