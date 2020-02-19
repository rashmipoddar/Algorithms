#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  quantity_possible = []
  for item in recipe:
    if item in ingredients:
      quantity_possible.append(ingredients[item] // recipe[item])
    else:
      return 0  
  minimum_quantity = quantity_possible[0]
  for num in quantity_possible:
    if num < minimum_quantity:
      minimum_quantity = num
  return minimum_quantity
    


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))