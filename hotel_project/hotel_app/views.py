from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm, AuthenticationForm
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from hotel_scraper.hotel_scraper.spiders.booking import BookingSpider
from hotel_scraper.hotel_scraper.spiders.agoda import AgodaSpider
from django.shortcuts import render
from .forms import SearchForm
from .models import Hotel
from .scraping import run_spiders 
from django.shortcuts import render
from .forms import SearchForm
from .models import Hotel
from .scraping import run_spiders  # Import the scraping function
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hotel, Bookmark
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm  
from .forms import SignUpForm 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Bookmark 

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('search')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def run_spiders(city):
    process = CrawlerProcess(get_project_settings())
    process.crawl(BookingSpider, city=city)
    process.crawl(AgodaSpider, city=city)
    process.start()
    


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            city = form.cleaned_data['city']
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']
            star_rating = form.cleaned_data['star_rating']

            # Run Scrapy spiders to scrape data
            run_spiders(city)

            # Filter hotels based on search criteria
            hotels = Hotel.objects.filter(
                city__icontains=city,
                price__gte=min_price,
                price__lte=max_price,
                star_rating=star_rating
            )
            return render(request, 'search_results.html', {'hotels': hotels})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('search')  # Redirect to search if logged in
    else:
        return redirect('login')  # Redirect to login if not logged in
    
    

@login_required
def bookmarks(request):
    """
    Display the user's bookmarked hotels.
    """
    # Get the current user's bookmarks
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmarks.html', {'bookmarks': bookmarks})

@login_required
def bookmark_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    Bookmark.objects.get_or_create(user=request.user, hotel=hotel)
    return redirect('search_results')