

from django.contrib import admin
from django.urls import path,include
from reminderlist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('reminderlist.urls')),
]
