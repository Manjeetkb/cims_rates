from django.urls import path
from django.contrib import admin
from . import views, include

urlpatterns = [
#   path('', include('home.urls')),
#   path('admin/', admin.site.urls),
   path('', views.home, name='home'),
 #  path('add', views.add, name='add'),

]