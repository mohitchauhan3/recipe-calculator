def recipe_cost_calculator():
    recipe_name = input("Enter the recipe name: ")
    serving_size = float(input("Enter the serving size: "))

    ingredients = []
    total_cost = 0.0

    num_ingredients = int(input("Enter the number of ingredients: "))

    for i in range(num_ingredients):
        ingredient_name = input(f"Enter the name of ingredient {i + 1}: ")
        amount = float(input(f"Enter the amount of {ingredient_name} needed (in units): "))
        cost_per_unit = float(input(f"Enter the cost of {ingredient_name} per unit: "))

        ingredient_cost = amount * cost_per_unit
        total_cost += ingredient_cost

        ingredients.append((ingredient_name, amount, cost_per_unit, ingredient_cost))

    cost_per_serving = total_cost / serving_size

    print("\n------------------------------------------")
    print(f"Recipe: {recipe_name}")
    print(f"Serving Size: {serving_size}")
    print("--------------------------------------------")
    for ingredient in ingredients:
        print(f"{ingredient[0]} - {ingredient[1]} units - ${ingredient[2]:.2f} per unit - Total Cost: ${ingredient[3]:.2f}")
    print("-------------------------------------------")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Cost per Serving: ${cost_per_serving:.2f}")


if __name__ == "__main__":
    recipe_cost_calculator()
