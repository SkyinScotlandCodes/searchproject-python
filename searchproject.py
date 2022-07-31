import requests
import config

# Register to get an APP ID and key https://developer.edamam.com/
app_id = config.application_id
app_key = config.application_key

includeAppId = "app_id={}".format(app_id)
includeAppKey = "app_key={}".format(app_key)
startPagination = "from=0"
endPagination = "to=10"

CuisineType_array = {"American", "British", "Caribbean", "Chinese", "French", "Italian", "Japanese", "Kosher",
                     "Mediterranean", "Mexican"}

# ask user to enter ingredient(s)
inputIngredient = input("Please enter one or more ingredients to search for: ")
# return invalid response if user enters nothing or only spaces
while inputIngredient == "" or inputIngredient.isspace():
    inputIngredient = input("Invalid Response. Please enter at least one or more ingredients. Try again: ")
# prints out choose ingredient/s
# print("You have chosen these ingredients: " + inputIngredient)

addIngredients = inputIngredient


# ask user to enter cuisine preference
inputCuisineType = input(
    f"Please enter choose a preferred cuisine from the following options below - \n{CuisineType_array}: ")
while inputCuisineType not in CuisineType_array:
    inputCuisineType = input(
        f"Invalid Response. Please enter choose a preferred cuisine from the following options below or type 'N' if none - \n{CuisineType_array}: ")
# print("You have chosen: " + inputCuisineType)

addCuisineType = inputCuisineType

print(f'You have searched for {inputCuisineType} recipes using {inputIngredient}')

r = requests.get(
    f"https://api.edamam.com/search?q={addIngredients}&cuisineType={addCuisineType}&{includeAppId}&{includeAppKey}&{startPagination}&{endPagination}")

data = r.json()
results = data['hits']

count = data['count']

print(f"{count} recipes found")

for result in results:
    recipe = result['recipe']
    print(recipe['label'])
    print(recipe['url'])
    print()
