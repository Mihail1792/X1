from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:shortened_part>', views.redirect_original_url, name='redirect'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
