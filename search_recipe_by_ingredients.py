import requests
import config

# Register to get an APP ID and key https://developer.edamam.com/
app_id = config.application_id
app_key = config.application_key

includeAppId = "app_id={}".format(app_id)
includeAppKey = "app_key={}".format(app_key)

# ask user to enter ingredient(s)
inputIngredient = input("Please enter one or more ingredients to search for: ")
# return invalid response if user enters nothing or only spaces
while inputIngredient == "" or inputIngredient.isspace():
    inputIngredient = input("Invalid Response. Please enter at least one or more ingredients. Try again: ")
# prints out choose ingredient/s
print("You have chosen these ingredients: " + inputIngredient)

addIngredients = inputIngredient
startPagination = "0"
endPagination = "10"

r = requests.get(
    f"https://api.edamam.com/search?q={addIngredients}&{includeAppId}&{includeAppKey}&from={startPagination}&to={endPagination}")

# Returns HTTP response status codes indicate whether a specific HTTP request has been successfully completed.
if r.status_code == 200:
    print("Your request was successful")
else:
    print("Error: " + str(r))

# # Returns json
# print(r.json())

data = r.json()

# Returns the total number of recipes found
print(data['count'])

# Returns the first result in json
print(data['hits'][0])

