from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import AboutMe, Skills, Services, Portfolio
from .forms import ContactForms
# Create your views here.
 


def index_view(request):
    # Retrieve data for AboutMe
    about_me_info = get_object_or_404(AboutMe)
    
    # Retrieve data for Skills
    skills = Skills.objects.all()
    
    # Retrieve data for Services
    services = Services.objects.all()
    
    # Retrieve data for Portfolio
    portfolio = Portfolio.objects.all()
    print(f"Portfolio: {portfolio}") 
    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            # Return a JSON response upon successful submission
            return JsonResponse({'message': 'Your message has been sent. Thank you!'})
        else:
            # Handle form errors
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)

    else:
        form = ContactForms()
    
    context = {
        'first_name': about_me_info.first_name,
        'last_name': about_me_info.last_name,
        'profession': about_me_info.profession,
        'email': about_me_info.email,
        'phone_number': about_me_info.phone_number,
        'github': about_me_info.github,
        'description': about_me_info.description,
        'skills': skills,
        'services': services,
        'portfolio': portfolio,
        'form': form  # Include the contact form in the context
    }
    
    return render(request, 'index.html', context)

def portfolio_detail_view(request, pk):
    project = get_object_or_404(Portfolio, pk=pk)
    about_me_info = get_object_or_404(AboutMe)

    context = {
        'project': project,
        'first_name': about_me_info.first_name,
        'last_name': about_me_info.last_name,
        'profession': about_me_info.profession,
        'email': about_me_info.email,
        'phone_number': about_me_info.phone_number,
        'github': about_me_info.github,
        'description': about_me_info.description,
    }
    return render(request, 'portfolio-details.html', context)