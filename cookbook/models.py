from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    favorite_by = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    order = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200, null=True, blank=True)
    needed_by = models.ManyToManyField(User, blank=True)

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

