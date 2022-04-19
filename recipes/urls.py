from django.urls import include, path

from recipes.views import contato, home, sobre

    #HTTP RESPONSE

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]

