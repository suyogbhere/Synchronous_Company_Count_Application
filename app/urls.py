from django.urls import path,include
from app import  views
from allauth.account import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static
from app import forms

urlpatterns=[
    path('', views.index, name='index'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html'),name='account_login'),   #LoginForm
    path('accounts/signup/',auth_views.SignupView.as_view(template_name='app/signup.html'),name='account_signup'),   #SignupForm
    path('accounts/logout/',auth_views.LogoutView.as_view(),name='account_logout'),
    path('upload_data/', views.upload_data, name='upload_data'),
    path('query_builder/', views.query_builder, name='query_builder'),
    path('users_list/', views.User_show, name='users_list'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
