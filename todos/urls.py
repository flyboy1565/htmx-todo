from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('create', add_task, name="create"),
    path('update/<int:pk>', update_todo, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
]