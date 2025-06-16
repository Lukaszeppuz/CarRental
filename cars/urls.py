from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('car/<car_id>', views.car, name='car'),
    path('categories', views.categories, name='categories'),
    path('category/<category_name>', views.category, name='category')
]