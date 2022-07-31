CuisineType_array = {"American", "British", "Caribbean", "Chinese", "French", "Italian", "Japanese", "Kosher",
                     "Mediterranean", "Mexican"}

CuisineType_array = [CuisineType_array.lower() for CuisineType_array in CuisineType_array]

# removed from CuisineType_array
# "Asian" "Central Europe"  "Eastern Europe" "Middle Eastern" "Nordic" "South American" "South East Asian"

# ask user to enter cuisine preference
inputCuisineType = input(
    f"Please enter choose a preferred cuisine from the following options below or type 'N' if none - \n{CuisineType_array}: ")
while (inputCuisineType != "N" and inputCuisineType != "n") and inputCuisineType not in CuisineType_array:
    inputCuisineType = input(
        f"Please enter choose a preferred cuisine from the following options below or type 'N' if none - \n{CuisineType_array}: ")
print("You have chosen: " + inputCuisineType)
