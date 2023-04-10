from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='registraion'),
    path('login/', views.AuthenticationView.as_view(), name='login'),
    path('users/', views.UserListView.as_view(), name='user_list'),
]