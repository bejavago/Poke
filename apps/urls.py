
from django.urls import path,include

from apps import views

urlpatterns = [
    path('', views.index ),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('pokes/<user_id>/', views.poke, name="poke"),   
]