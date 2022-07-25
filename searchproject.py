import requests


def recipe_search(ingredient):
    app_id = '7b009ee0'
    app_key = '5929f995b6fda7c2e998943fa9abc48e'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print()

run()
