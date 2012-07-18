from django.shortcuts import render_to_response, redirect
from cookbook.models import Recipe, Favorite

def index(request):
    all_recipes = Recipe.objects.all()
    return render_to_response('recipes/index.html', {'all_recipes': all_recipes})

def recipe_detail(request, name):
    try:
        recipe = Recipe.objects.get(slug=name)
    except Recipe.DoesNotExist:
        raise Http404
    favorites = Favorite.objects.filter(user=request.user)
    my_fav = False
    for fav in favorites:
        if fav.recipe == recipe:
            my_fav = True
    return render_to_response('recipes/detail.html', {'recipe': recipe, 'my_fav': my_fav})

def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render_to_response('recipes/favorites.html', {'favorites': favorites})

def add_favorite(request, name):
    try:
        fav_recipe = Recipe.objects.get(slug=name)
    except Recipe.DoesNotExist:
        raise Http404
    new_favorite = Favorite(recipe=fav_recipe, user=request.user)
    new_favorite.user = request.user
    new_favorite.save()
    return redirect('/recipes/favorites/')

def delete_favorite(request, name):
    try:
        fav_recipe = Recipe.objects.get(slug=name)
    except Recipe.DoesNotExist:
        raise Http404
    try:
        old_favorite = Favorite.objects.get(recipe=fav_recipe)
    except Favorite.DoesNotExist:
        raise Http404
    old_favorite.delete()
    return redirect('/recipes/favorites/')
