
from django.contrib import admin
from django.urls import path
from app.views import employeeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee/',employeeListView),
]
