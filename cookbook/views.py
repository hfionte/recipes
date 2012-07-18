from django.shortcuts import render_to_response, redirect
from cookbook.models import Recipe

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
