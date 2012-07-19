from django.shortcuts import render_to_response, redirect
from cookbook.models import Recipe, Ingredient

def index(request):
    all_recipes = Recipe.objects.all()
    user = request.user
    return render_to_response('recipes/index.html', {'all_recipes': all_recipes, 'user': user})

def recipe_detail(request, name):
    try:
        recipe = Recipe.objects.get(slug=name)
    except Recipe.DoesNotExist:
        raise Http404
    favorite_by_users = recipe.favorite_by.all()
    my_fav = request.user in favorite_by_users
    return render_to_response('recipes/detail.html', {'recipe': recipe, 'my_fav': my_fav})

def favorites(request):
    favorites = Recipe.objects.filter(favorite_by=request.user)
    return render_to_response('recipes/favorites.html', {'favorites': favorites})

def add_favorite(request, name):
    try:
        fav_recipe = Recipe.objects.get(slug=name)
    except Recipe.DoesNotExist:
        raise Http404
    fav_recipe.favorite_by.add(request.user)
    fav_recipe.save()
    return redirect('/recipes/favorites/')

def delete_favorite(request, name):
    try:
        fav_recipe = Recipe.objects.get(slug=name)
    except Recipe.DoesNotExist:
        raise Http404
    fav_recipe.favorite_by.remove(request.user)
    fav_recipe.save()
    return redirect('/recipes/favorites/')

def shopping_list(request):
    needed_ingredients = Ingredient.objects.filter(needed_by=request.user)
    return render_to_response('recipes/shopping-list.html', {'ingredients': needed_ingredients})

def add_ingredient(request, item_id):
    try:
        list_ingredient = Ingredient.objects.get(pk=item_id)
    except Ingredient.DoesNotExist:
        raise Http404
    list_ingredient.needed_by.add(request.user)
    list_ingredient.save()
    return redirect('/shopping-list/')

def delete_ingredient(request, item_id):
    try:
        list_ingredient = Ingredient.objects.get(pk=item_id)
    except Ingredient.DoesNotExist:
        raise Http404
    list_ingredient.needed_by.remove(request.user)
    list_ingredient.save()
    return redirect('/shopping-list/')
