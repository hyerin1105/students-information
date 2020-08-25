from django.urls import path, include
from .views import index, create, detail, delete, update, my_index

urlpatterns = [
    path('', index, name='index'),
    path('my_index/', my_index, name="my_index"),
    path('create/', create, name='create'),
    path('detail/<int:inf_id>', detail, name='detail'),
    path('delete/<int:inf_id>', delete, name='delete'),
    path('update/<int:inf_id>', update, name='update'),
]