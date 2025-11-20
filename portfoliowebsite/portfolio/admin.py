from django.contrib import admin
from .models import skills, Services, PortfolioItem
# Register your models here.
admin.site.register(skills) 
admin.site.register(Services)
admin.site.register(PortfolioItem)