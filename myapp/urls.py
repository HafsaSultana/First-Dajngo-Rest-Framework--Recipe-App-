from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views
from knox import views as knox_views



urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),

    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('recipe/', views.RecipeList.as_view()),
    path('recipe/<int:pk>/', views.Details_Recipe.as_view()),

    path('family/', views.Family.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)