import requests
import config

# Register to get an APP ID and key https://developer.edamam.com/
app_id = config.application_id
app_key = config.application_key

includeAppId = "app_id={}".format(app_id)
includeAppKey = "app_key={}".format(app_key)

# ask user to enter ingredient(s)
ingredient = input("Please enter one or more ingredients to search for: ")
# return invalid response if user enters nothing or only spaces
while ingredient == "" or ingredient.isspace():
    ingredient = input("Invalid Response. Please enter at least one or more ingredients. Try again: ")
ingredients_selected = "You have chosen these ingredients = " + ingredient
print(ingredients_selected)

addIngredients = ingredient

r = requests.get("https://api.edamam.com/search?q={}&{}&{}".format(addIngredients, includeAppId, includeAppKey))

# Returns HTTP response status codes indicate whether a specific HTTP request has been successfully completed.
print(r)
print("Your request was successful")

# # Returns json
# print(r.json())
data = r.json()

# Returns the first result in json
print(data['hits'][0])

# Returns the total number of recipes found
print(data['count'])