from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Company_data)
class Company_data_Admin(admin.ModelAdmin):
    list_display = ['id','name','domain','year_founded','industry','size_range','locality','country','linkedin_url','current_employee_estimate','total_employee_estimate']