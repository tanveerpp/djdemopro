from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('addtrainer', views.addtrainer),
    path('deletetrainer', views.deletetrainer),
    path('updatetrainer', views.updatetrainer),
    path('addstudent', views.addstudent),
    path('deletestudent', views.deletestudent),
    path('updatestudent', views.updatestudent),
]
