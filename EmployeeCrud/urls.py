
from django.contrib import admin
from django.urls import path
from app.views import employeeListView,userListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee/',employeeListView),
    path('api/users/',userListView),
]
