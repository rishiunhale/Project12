
from django.contrib import admin
from django.urls import path
from wordcount import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',views.homepage, name="home"),
path('Contact/',views.contact),
    path('count/',views.count, name='count'),
]
