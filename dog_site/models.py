from django.db import models

# Create your models here.
from django.urls import reverse


class Dog(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dog', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
        ordering = ['title']


# class DogImage(models.Model):
#     dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
#
#     def __str__(self):
#         return self.dog.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Carousel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CarouselImage(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class PhotoGallery(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PhotoGalleryImage(models.Model):
    photo_gallery = models.ForeignKey(PhotoGallery, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.caption
