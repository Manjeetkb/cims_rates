from django.urls import path
from django.contrib import admin
from . import views, include

urlpatterns = [
#    path('',views.home, name='home')
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]