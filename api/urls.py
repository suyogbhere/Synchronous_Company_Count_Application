from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api import views


# Create a router and register your ViewSet
router = DefaultRouter()
router.register('companydata',views.CompanyDataViewset, basename='company_data'),
router.register('fileupload',views.FileViewset, basename='file_upload'),


urlpatterns=[
    path('',include(router.urls)),
]