from django.urls import path
from .import views

urlpatterns = [

    
    
    
    path("login/", views.loginpage, name="login"),
    path("register/", views.registerpage, name="register"),
    path("logout/", views.logoutuser, name="logout"),

    path("values/", views.valuess, name="values"),
    path("sensor/", views.sensors, name="sensors"),
    path("", views.home, name="home"),
    path("site1/", views.site1, name="site1"),
    path("site2/", views.site2, name="site2"),
    path("site1m/", views.site1m, name="site1m"),
    path("site2m/", views.site2m, name="site2m"),
    path("site3/", views.site3, name="site3"),
    path("home/", views.home, name="home"),

    path('download2/', views.download_file2, name="Download2"),
    path('download3/', views.download_file3, name="Download3"),
    
    path("view/", views.view, name="create"),
]