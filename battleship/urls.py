from django.urls import path

from . import views

app_name = 'battleship'

urlpatterns = [
    path("<int:game_id>", views.index, name='index')
]
