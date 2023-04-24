from django.urls import path, include
from api.core.views import todo_list, todo_detail_change_delete

urlpatterns = [
    path('', todo_list, name="todo_list"),
    path('<int:pk>/', todo_detail_change_delete, name="todo_detail_change_delete"),

]