from django.urls import path
from . import views

urlpatterns = [
    # Home page (redirect to search if logged in, else login)
    path('', views.home, name='home'),
    
    # Authentication URLs
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Search and Bookmarks
    path('search/', views.search, name='search'),
    path('bookmark/<int:hotel_id>/', views.bookmark_hotel, name='bookmark_hotel'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
]