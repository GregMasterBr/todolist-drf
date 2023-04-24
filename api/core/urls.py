from django.urls import path, include
#from api.core.views import todo_list, todo_detail_change_delete
#Refatorado com a classed based view
from api.core.views import  TodoListAndCreate, TodoDetailChangeAndDelete

urlpatterns = [
    # path('todo_list/', todo_list, name="todo_list"),
    # path('<int:pk>/', todo_detail_change_delete, name="todo_detail_change_delete"),
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),


]