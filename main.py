def recipe_calcuator():
  recipe_name = input("enter the recipe name: ")
  serving_size = int(input("enter the serving size: "))

  ingredients = []
  total_cost = 0.0
  
  num_ingredients = int(input("enter the number of ingredients: "))
  
  for i in range(num_ingredients):
    ingredients_name = input(f"enter the name of ingredients {i + 1
    }: ") 
    amount = float(input(f"enter the amunt of {ingredients_name} needed (in units): "))
    ingredinet_cost = amount * cost_per_unit
    total_cost += ingredient_cost
    
    ingredients.append((ingredients_name, amount, cost_per_unit, ingredinet_cost))
    cost_per_serving = total_cost / serving_size
  
