from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Avg, Count
from .models import TravelPackage, Review, TravelExperience, Destination, TravelRequest, TravelFeedback


def home(request):
    """Home page showing featured packages and recent reviews"""
    featured_packages = TravelPackage.objects.filter(is_featured=True)[:6]
    recent_reviews = Review.objects.select_related('package', 'user')[:3]
    destinations_count = Destination.objects.count()
    packages_count = TravelPackage.objects.count()
    
    context = {
        'featured_packages': featured_packages,
        'recent_reviews': recent_reviews,
        'destinations_count': destinations_count,
        'packages_count': packages_count,
    }
    return render(request, 'travel/home.html', context)


def latest_offers(request):
    """Latest travel offers and packages"""
    # Simple view for the latest offers page
    context = {}
    return render(request, 'travel/latest_offers_new.html', context)


def i_want_to_travel(request):
    """Travel planning and booking form page"""
    form_submitted = False
    
    if request.method == 'POST':
        # Process the form data
        people_count = request.POST.get('people_count')
        has_kids = request.POST.get('has_kids')
        travel_dates = request.POST.get('travel_dates')
        destination = request.POST.get('destination')
        requirements = request.POST.get('requirements')
        
        # Save the travel request to the database
        TravelRequest.objects.create(
            people_count=people_count,
            has_kids=has_kids,
            travel_dates=travel_dates,
            destination=destination,
            requirements=requirements
        )
        
        form_submitted = True
    
    context = {
        'form_submitted': form_submitted,
    }
    return render(request, 'travel/travel_form_new.html', context)


def i_already_travelled(request):
    """Travel feedback form page"""
    form_submitted = False
    
    if request.method == 'POST':
        # Process the feedback form data
        experience = request.POST.get('experience')
        improvement = request.POST.get('improvement')
        
        # Save the travel feedback to the database
        TravelFeedback.objects.create(
            experience=experience,
            improvement=improvement
        )
        
        form_submitted = True
    
    context = {
        'form_submitted': form_submitted,
    }
    return render(request, 'travel/feedback_form.html', context)


def reviews(request):
    """Customer reviews and testimonials"""
    reviews_list = Review.objects.select_related('user', 'package', 'package__destination').order_by('-created_at')
    
    # Get the most recent reviews to display
    featured_reviews = reviews_list[:6]  # Show up to 6 reviews
    
    context = {
        'reviews': featured_reviews,
    }
    return render(request, 'travel/reviews_new.html', context)
