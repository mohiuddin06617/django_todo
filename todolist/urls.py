from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todo/<int:todo_id>/',views.details,name="detail")
]
