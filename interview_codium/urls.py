from django.contrib import admin
from django.urls import include, path
from polls import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('taskData', views.TodoView,)

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]