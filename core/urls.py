from django.contrib.auth import views as auth_views
from django.urls import path
from .views import custom_logout

from . import views

urlpatterns = [
    path('', views.frontpage, name="frontpage"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', custom_logout, name="logout"),
]