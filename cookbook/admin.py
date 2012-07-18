from django.contrib import admin
from cookbook.models import Recipe, Ingredient, Step, Note, Favorite

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 3

class StepInline(admin.TabularInline):
    model = Step
    extra = 3

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1

class StepInline(admin.TabularInline):
    model = Step
    extra = 3

class RecipeAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'description']
    inlines = [IngredientInline, StepInline, NoteInline]
    list_display = ('title', 'description')
    prepopulated_fields = {"slug": ("title",)}

class FavoriteAdmin(admin.ModelAdmin):
    fields = ['user', 'recipe']
    list_display = ('user', 'recipe')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
