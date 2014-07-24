from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'visualization.views.index'),
    url(r'bubble_sort', 'visualization.views.single_array_in_place_algorithm'),
)
