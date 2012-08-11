import json
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from cookbook.models import Recipe, RecipeTag, Ingredient
from django.contrib.auth.decorators import login_required
from django.core import serializers

def index(request):
    all_recipes = Recipe.objects.all()
    user = request.user
    return render_to_response('recipes/index.html', {'all_recipes': all_recipes, 'user': user})

def index_by_tag(request):
    all_tags = RecipeTag.objects.all()
    user = request.user
    return render_to_response('recipes/index_by_tag.html', {'all_tags': all_tags, 'user': user})

def index_json(request):
    #all_recipes = Recipe.objects.all()
    #data = serializers.serialize('json', all_recipes)
    #return HttpResponse(data)
    all_recipes = Recipe.objects.all()
    user = request.user
    return render_to_response('recipes/index-json.html',
        {'all_recipes': all_recipes, 'user': user},
        mimetype="application/json"
    )

def recipe_detail(request, name):
    try:
        recipe = Recipe.objects.get(slug=name)
    except Recipe.DoesNotExist:
        raise Http404
    favorite_by_users = recipe.favorite_by.all()
    my_fav = request.user in favorite_by_users
    user = request.user
    return render_to_response('recipes/detail.html', {'recipe': recipe, 'my_fav': my_fav, 'user': user})

@login_required
def favorites(request):
    favorites = Recipe.objects.filter(favorite_by=request.user)
    user = request.user
    return render_to_response('recipes/favorites.html', {'favorites': favorites, 'user': user})

@login_required
def add_favorite(request, name):
    try:
        fav_recipe = Recipe.objects.get(slug=name)
    except Recipe.DoesNotExist:
        raise Http404
    fav_recipe.favorite_by.add(request.user)
    fav_recipe.save()
    return redirect('/recipes/favorites/')

@login_required
def delete_favorite(request, name):
    try:
        fav_recipe = Recipe.objects.get(slug=name)
    except Recipe.DoesNotExist:
        raise Http404
    fav_recipe.favorite_by.remove(request.user)
    fav_recipe.save()
    return redirect('/recipes/favorites/')

@login_required
def shopping_list(request):
    user = request.user
    needed_ingredients = Ingredient.objects.filter(needed_by=user)
    return render_to_response('recipes/shopping-list.html', {'ingredients': needed_ingredients, 'user': user})

@login_required
def add_ingredient(request, item_id):
    user = request.user
    try:
        list_ingredient = Ingredient.objects.get(pk=item_id)
    except Ingredient.DoesNotExist:
        raise Http404
    list_ingredient.needed_by.add(user)
    list_ingredient.save()
    recipe = list_ingredient.recipe
    return render_to_response('recipes/ingredient_list.html', {'recipe': recipe, 'user': user})

@login_required
def delete_ingredient(request, item_id, from_where):
    user = request.user
    try:
        list_ingredient = Ingredient.objects.get(pk=item_id)
    except Ingredient.DoesNotExist:
        raise Http404
    list_ingredient.needed_by.remove(request.user)
    list_ingredient.save()
    if from_where == "-from-recipe":
        recipe = list_ingredient.recipe
        return render_to_response('recipes/ingredient_list.html', {'recipe': recipe, 'user': user})
    else:
        needed_ingredients = Ingredient.objects.filter(needed_by=user)
        return render_to_response('recipes/shopping_list_items.html', {'ingredients': needed_ingredients, 'user': user})

