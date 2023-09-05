from django.urls import path
from food_app import views

urlpatterns = [
    path('',views.index ,name = "index"),
    path("create/",views.create,name = 'create'),
    path("view_all/",views.view_all,name = 'view_all'),
    path("update/<int:id>",views.update,name = 'update'),
    path("delete/<int:id>",views.delete,name = 'delete'),

   
]