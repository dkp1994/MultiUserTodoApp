from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('signin/',views.signin, name='signin'),
    path('logout/',views.userlogout, name='logout'),
    path('add-todo/',views.add_todo, name='add-todo'),
    path('delete-todo/<str:id>',views.delete_todo, name='delete-todo'),
    path('change-status/<str:id>/<str:status>',views.change_todo, name='change-status'),
]