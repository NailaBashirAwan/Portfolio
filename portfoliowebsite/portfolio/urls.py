from django.contrib import admin
from django.urls import path
from . import views
from portfolio.views import starter_page,index,about,services,contact,portfolio,portfolio_details,resume
#from portfolio.views import starter_page,index,about,services,contact,portfolio,portfolio_details,resume
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('start/', starter_page, name='starter_page'),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio_details/', portfolio_details, name='portfolio_details'),
    path('resume/', resume, name='resume'),
    
]