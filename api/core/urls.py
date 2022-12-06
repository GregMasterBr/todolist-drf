from django.urls import path, include
from api.core.views import todo_list

urlpatterns = [
    path('', todo_list, name="todo_list")

]