from django.shortcuts import render
from django.http import HttpResponseBadRequest

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, recipe_name):
    recipe = DATA.get(recipe_name)
    
    if not recipe:
        return HttpResponseBadRequest("Рецепт не найден.")
    
    servings = request.GET.get('servings')
    
    if servings:
        try:
            servings = int(servings)
            if servings <= 0:
                raise ValueError
        except ValueError:
            return HttpResponseBadRequest("Параметр servings должен быть положительным целым числом.")
        
        recipe = {ingredient: quantity * servings for ingredient, quantity in recipe.items()}
    
    context = {
        'recipe': recipe
    }
    
    return render(request, 'calculator/index.html', context)