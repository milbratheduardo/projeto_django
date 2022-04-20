from django.urls import include, path

from recipes.views import home

    #HTTP RESPONSE

urlpatterns = [
    path('', home),

]

