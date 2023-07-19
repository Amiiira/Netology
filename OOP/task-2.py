from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        num_serving = int(file.readline())
        ingredients = []
        for i in range(num_serving):
            ing = file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            ingredient = {
                'ingredient_name' : ingredient_name,
                'quantity' : quantity,
                'measure' : measure
            }
            ingredients.append(ingredient)
        file.readline()
        cook_book[dish_name] = ingredients
pprint(cook_book,sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_needed = {}
    for dish in dishes:
        recipe = cook_book[dish]
        for i in range(len(recipe)):
            ings = recipe[i]
            name = ings.pop('ingredient_name')
            quantity = int(ings['quantity']) * person_count
            ings['quantity'] = quantity
            if name in ingredients_needed:
                ingredients_needed[name]['quantity'] +=  quantity 
            else:
                ingredients_needed[name] = ings
    
    # pprint(ingredients_needed)
        
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

sum_text = {}

with open('1.txt', 'rt', encoding='utf-8') as file:
    content_1 = file.readlines()
    sum_1 = len(content_1)
    sum_text[sum_1] = content_1

with open('2.txt', 'rt', encoding='utf-8') as file:
    content_2 = file.readlines()
    sum_2 = len(content_2)
    sum_text[sum_2] = content_2

with open('3.txt', 'rt', encoding='utf-8') as file:
    content_3 = file.readlines()
    sum_3 = len(content_3)
    sum_text[sum_3] = content_3

sums = [sum_1, sum_2, sum_3]

with open('final.txt', 'wt', encoding='utf-8') as file:
    sums.sort()
    for i in range(len(sums)):
        file.write(f'{i+1}.txt\n')
        file.write(f'{sums[i]}\n')
        file.writelines(sum_text[sums[i]])
        file.write('\n')