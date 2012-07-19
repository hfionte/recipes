from django.contrib import admin
from cookbook.models import Recipe, Ingredient, Step, Note

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 3
    fields = ['order', 'name', 'quantity']

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

admin.site.register(Recipe, RecipeAdmin)
