from django.shortcuts import render, redirect
from .models import EventList, AboutPage, TeamMembers,AboutUs, TestimonialSection, DonateModel, MediaLibrary, Banner
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
import threading
# Create your views here.

class EmailThread(threading.Thread):
    def __init__(self, subject, message, from_email, to_email):
        self.subject = subject
        self.message = message
        self.from_email = from_email
        self.to_email = to_email
        threading.Thread.__init__(self)

    def run(self):
        send_mail(
            self.subject,
            self.message,
            self.from_email,
            self.to_email,
            fail_silently=True,
        )
        print('Email sent successfully')

def Home(request):
    banners = Banner.objects.all()
    events = EventList.objects.all()[:4]
    about = AboutUs.objects.first()
    review = TestimonialSection.objects.all()
    context = {'banners':banners, 'events': events, 'about':about, 'review':review}
    return render(request, 'main/home.html', context)

def EventDetails(request,slug):
    events = EventList.objects.get(slug=slug)
    context = {'events':events}
    return render(request, 'main/event_details.html',context)

def EventView(request):
    events = EventList.objects.all()
    context = {'events':events}
    return render(request, 'main/event_list.html', context)

def AboutView(request):
    texts = AboutPage.objects.first()
    print(texts)
    teams = TeamMembers.objects.all()
    context = {'text':texts, 'teams':teams}
    return render(request, 'main/about.html', context)

def ContactView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            client_message = form.cleaned_data.get('message')
            form.save()
            messages.success(request, "Message sent successfully")

            subject = 'You received a new message from SSOB'
            message = f'Hi {client_message}'
            from_email = settings.EMAIL_HOST_USER
            to_email = [form.cleaned_data.get('email')]

            # Start a new thread to send the email
            thread = EmailThread(subject, message, from_email, to_email)
            thread.start()

            return redirect('main:contact')

    context = {'form': form}
    return render(request, 'main/contact.html', context)


def MediaLibraryView(request):
    event_img = MediaLibrary.objects.filter(media_year='2023')
    event_name_list = MediaLibrary.objects.all()
    context = {'event_img':event_img, 'event_name_list':event_name_list}
    return render(request, 'main/media_library.html', context)

def PhotoDetailView(request, id):
    name = MediaLibrary.objects.get(id=id)
    photos = MediaLibrary.objects.filter(event_name=name.event_name)
    context = {'name':name, 'photos':photos}
    return render(request, 'main/photo_detail.html', context)

def DonationView(request):
    donate_list = DonateModel.objects.all()
    context = {'donates':donate_list}
    return render(request, 'main/donate.html', context)

