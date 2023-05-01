from django.urls import path
from . import views

urlpatterns = [path("", views.menu, name = "menu"),
               path("menu/menu2", views.menu2, name = "menu2"),
               

]