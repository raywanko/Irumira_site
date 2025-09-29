from django.contrib import admin
from .models import CompanyInfo, Recruitment

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'updated_at']
    search_fields = ['name', 'email']

@admin.register(Recruitment)
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'
