from django.urls import include, path

from . import views

    #HTTP RESPONSE

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipes)

]

