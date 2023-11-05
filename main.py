# This programme asks users for the name of the recipe and the serving size

# asking the users name
print("Hello welcome to recipe calculator what is your name ")
n = input()
print("welcome to recipe calculator " + n)


#showing the instruction.
def show_instructions():
  print("\n would you like some basic instructions on to us this program ")
  answer = input("please answer Yes or No.").lower()

  if answer == "yes":
    print(
        "1.Your instructions are that this programe will ask for a recipe name and serving size.\n2.list of each ingredients the amonut of the ingredint need and the cost of that ingredient.\n3. At end it will work out the cost per serving."
    )

  elif answer == "no":
    print("Okay")

  else:
    print("please answer with Yes and No.")
    show_instructions()


show_instructions()


def recipe_cost_calculator():
  recipe_name = input("Enter the recipe name: ")
  serving_size = float(input("Enter the serving size: "))

  # requesting the user to input the name of the recipe and serving

  ingredients = []
  total_cost = 0.0

  # how many ingredients will be utilised

  num_ingredients = int(input("Enter the number of ingredients: "))

  for i in range(num_ingredients):
    ingredient_name = input(f"Enter the name of ingredient {i + 1}: ")
    amount = float(
        input(f"Enter the amount of {ingredient_name} needed (in G): "))
    cost_per_unit = float(
        input(f"Enter the cost of {ingredient_name} per G: "))

    # requesting the user for the pricing and the ingredients

    ingredient_cost = amount * cost_per_unit
    total_cost += ingredient_cost

    # multiplied by the component price and the price per unit

    ingredients.append(
        (ingredient_name, amount, cost_per_unit, ingredient_cost))

  cost_per_serving = total_cost / serving_size

  print("\n------------------------------------------")
  print(f"Recipe: {recipe_name}")
  print(f"Serving Size: {serving_size}")
  print("--------------------------------------------")
  for ingredient in ingredients:
    print(
        f"{ingredient[0]} - {ingredient[1]} Grams - ${ingredient[2]:.2f} per Grams - Total Cost: ${ingredient[3]:.2f}")
  print("-------------------------------------------")
  print(f"Total Cost: ${total_cost:.2f}")
  print(f"Cost per Serving: ${cost_per_serving:.2f}")


# displaying the final results for the overall cost and the cost per serving size

if __name__ == "__main__":
  recipe_cost_calculator()
