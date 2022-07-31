# ask user to enter ingredient(s)
inputIngredient = input("Please enter one or more ingredients to search for: ")
# return invalid response if user enters nothing or only spaces
while inputIngredient == "" or inputIngredient.isspace():
    inputIngredient = input("Invalid Response. Please enter at least one or more ingredients. Try again: ")
# prints out choose ingredient/s
print("You have chosen these ingredients: " + inputIngredient)
