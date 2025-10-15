from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [
    path('', views.home, name='home'),
    path('latest-offers/', views.latest_offers, name='latest_offers'),
    path('i-want-to-travel/', views.i_want_to_travel, name='i_want_to_travel'),
    path('i-already-travelled/', views.i_already_travelled, name='i_already_travelled'),
    path('reviews/', views.reviews, name='reviews'),
]