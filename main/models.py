from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify

# Create your models here.
class EventList(models.Model):
    event_name = models.CharField(max_length=264)
    introduction = models.TextField(blank=True, null=True)
    schedule = models.TextField(blank=True, null= True)
    donation = models.TextField(blank=True, null=True)
    culture_program = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to='event_images')
    event_date = models.CharField(max_length=50, blank=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.event_name)
        super(EventList, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.event_name

class Banner(models.Model):
    image = models.ImageField(upload_to='banner')

class AboutUs(models.Model):
    title = models.CharField(max_length=264, blank=True, null=True)
    text = models.TextField()
    images = models.ImageField(upload_to='about-us-home', blank=True, null=True)


class AboutPage(models.Model):
    title = models.CharField(max_length=264, blank=True, null=True)
    text = models.TextField()
    images = models.ImageField(upload_to='about-us', blank=True, null=True)

class TeamMembers(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=264)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=64)
    profile_pic = models.ImageField(upload_to='team_members', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class TestimonialSection(models.Model):
    name = models.CharField(max_length=64)
    text = models.CharField(max_length=600)
    image = models.ImageField(upload_to='testimonial', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=264)
    subject = models.CharField(max_length=264)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

class DonateModel(models.Model):
    name = models.CharField(max_length=50)
    price_range = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='donation')

    def __str__(self) -> str:
        return self.name  

# class Category(models.Model):
#     name = models.CharField(max_length=64)
#     slug = models.SlugField(unique=True, blank=True)

#     def save(self,*args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super(Category, self).save(*args, **kwargs)
            

class MediaLibrary(models.Model):
    event_name = models.ForeignKey(EventList, on_delete=models.CASCADE)
    videos = models.FileField(upload_to='media_video', blank=True, null=True)
    photos = models.ImageField(upload_to='media_photo', blank=True, null=True)
    media_year = models.CharField(max_length=50, help_text='2021')

    def __str__(self) -> str:
        return self.event_name.event_name