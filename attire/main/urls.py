from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("register", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("profile", views.profile, name="profile"),
    path('logout/', views.logout_view, name='logout'),
]