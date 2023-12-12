from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Home, name='home'),
    path('event-details/<str:slug>/', views.EventDetails, name='event-details'),
    path('all-events/', views.EventView, name='event'),
    path('about-us/', views.AboutView, name='about'),
    path('contact-us/', views.ContactView, name='contact'),
    path('event-photos-videos/', views.MediaLibraryView, name='media'),
    path('photo-details/<int:id>/', views.PhotoDetailView, name='photo-detail'),
    path('membership-donation/', views.DonationView, name='donate'),
]
