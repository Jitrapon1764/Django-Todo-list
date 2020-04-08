from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTask, name='add'),
    path('complete/<task_id>', views.checkComplete , name='complete'),
    path('uncomplete/<task_id>', views.checkUnComplete , name='Uncomplete'),
    path('delete/<task_id>',views.delete,name='delete',)
]