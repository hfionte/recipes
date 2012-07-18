from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    order = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.name

class Step(models.Model):
    recipe = models.ForeignKey(Recipe)
    order = models.IntegerField(blank=True, null=True)
    step_text = models.TextField()

    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.step_text

class Note(models.Model):
    recipe = models.ForeignKey(Recipe)
    note_text = models.TextField()

    def __unicode__(self):
        return self.note_text

class Favorite(models.Model):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)

