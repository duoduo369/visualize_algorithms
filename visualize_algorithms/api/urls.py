from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'(?P<algorithm_name>(bubble_sort|a))$', views.SingleArrayInPlaceAlgorithmView.as_view()),
)
