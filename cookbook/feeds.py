from django.contrib.syndication.views import Feed
from cookbook.models import Recipe

class AllRecipesFeed(Feed):
    title = "All Recipes"
    link = "/"
    description = "All Recipes in the Cookbook."

    def items(self):
        return Recipe.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
