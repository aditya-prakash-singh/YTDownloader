from django.contrib import admin
from django.urls import path
from app import views 

urlpatterns = [
    path("returnn",views.returnn,name="run"),
    path("yourvid",views.yourvid,name="run"),
    path("",views.mainn,name="home"),
    path('admin/', admin.site.urls),
]