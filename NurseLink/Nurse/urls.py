from django.urls import path
from . import views

urlpatterns = [
    path("", views.nurse_landing, name="nurse_landing"),
    path("onboard/", views.nurse_onboard, name="nurse_onboard"),
    path("login/", views.nurse_login, name="nurse_login"),
    path("logout/", views.nurse_logout, name="nurse_logout"),
    path('home/', views.nurse_home, name="nurse_home"),
]
