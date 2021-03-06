from django.conf.urls import patterns, include, url
from cookbook.feeds import AllRecipesFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipes.views.home', name='home'),
    # url(r'^recipes/', include('recipes.foo.urls')),
    url(r'^$', 'cookbook.views.index'),
    url(r'^recipes-by-tag/$', 'cookbook.views.index_by_tag'),
    url(r'^recipes/favorites/$', 'cookbook.views.favorites'),
    url(r'^recipes/(?P<name>[-\w]+)/$', 'cookbook.views.recipe_detail'),
    url(r'^recipes/(?P<name>[-\w]+)/add-favorite/$', 'cookbook.views.add_favorite'),
    url(r'^recipes/(?P<name>[-\w]+)/delete-favorite/$', 'cookbook.views.delete_favorite'),
    url(r'^shopping-list/$', 'cookbook.views.shopping_list'),
    url(r'^shopping-list/(?P<item_id>\d+)/add/$', 'cookbook.views.add_ingredient'),
    url(r'^shopping-list/(?P<item_id>\d+)/delete(?P<from_where>[-\w]+)/$', 'cookbook.views.delete_ingredient'),

    # Feeds:
    url(r'^feeds/recipes$', AllRecipesFeed()),
    url(r'^json/recipes$', 'cookbook.views.index_json'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
