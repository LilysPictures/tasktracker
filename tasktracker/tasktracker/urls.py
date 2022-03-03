
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls', namespace='tasks')),
    path('admin/', admin.site.urls),
]
