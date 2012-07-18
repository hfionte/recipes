from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipes.views.home', name='home'),
    # url(r'^recipes/', include('recipes.foo.urls')),
    url(r'^recipes/$', 'cookbook.views.index'),
    url(r'^recipes/favorites/$', 'cookbook.views.favorites'),
    url(r'^recipes/(?P<name>[-\w]+)/$', 'cookbook.views.recipe_detail'),
    url(r'^recipes/(?P<name>[-\w]+)/add-favorite/$', 'cookbook.views.add_favorite'),
    url(r'^recipes/(?P<name>[-\w]+)/delete-favorite/$', 'cookbook.views.delete_favorite'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
