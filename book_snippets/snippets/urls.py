from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.CreateSnippetView.as_view(), name='create-snippet'),

]
