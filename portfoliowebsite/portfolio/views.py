from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import skills
from .models import Services
from .models import PortfolioItem

# Create your views here.
def starter_page(request):
    return render(request, 'starter-page.html')
def index(request):
    return render(request, 'index.html')
def about(request):
    if request.method == 'GET':
        skillsdata=skills.objects.all()
        
    context = {
        'skillsdata': skillsdata
    }
    return render(request, 'about.html', context)
def services(request):
    if request.method == 'GET':
        servicesdata=Services.objects.all()
    context = {
        'servicesdata': servicesdata
    }  
    return render(request, 'services.html', context) 

def portfolio(request):
    if request.method == 'POST' or request.method == 'GET':
        projects = PortfolioItem.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio.html',context)

def portfolio_details(request):
    return render(request, 'portfolio-details.html')    
def resume(request):
    return render(request, 'resume.html')   
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} <{email}>:\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                ['nailabashir1706@gmail.com'],  # receiver
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending message: {e}')
        return redirect('contact') 
    return render(request, 'contact.html')
