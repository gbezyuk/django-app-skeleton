from .models import NewsItem
from django.contrib import admin
from django.conf import settings
import os
from common.admin import CustomModelAdmin
from common.admin.actions import export_as_csv

class NewsItemAdmin(admin.ModelAdmin):
	pass
    
admin.site.register(NewsItem, NewsItemAdmin)