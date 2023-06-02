# Create your views here.
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Carousel, Dog, PhotoGallery, Post


class Home(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['dogs'] = Dog.objects.all()[:8]
        context['carousel'] = Carousel.objects.first()
        context['title'] = 'Главная'
        return context


class Posts(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 2
    allow_empty = False

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context


class Dogs(ListView):
    model = Dog
    template_name = 'dogs-page.html'
    context_object_name = 'dogs'
    paginate_by = 2
    allow_empty = False

    def get_queryset(self):
        return Dog.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'single-news.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        context['posts'] = Post.objects.all()[:10]
        context['dogs'] = Dog.objects.all()
        return context


class GetDog(DetailView):
    model = Dog
    template_name = 'single-dog.html'
    context_object_name = 'dog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Питомцы'
        context['dogs'] = Dog.objects.all()[:6]
        return context


def about(request):
    return render(request, 'about.html')


def receipt(request):
    return render(request, 'receipt.html')


def achivements(request):
    return render(request, 'photos.html')


class PhotosGallery(ListView):
    model = PhotoGallery
    template_name = 'photos.html'
    #context_object_name = 'photos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        context['photos'] = PhotoGallery.objects.first()
        return context


def contacts(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        sender = request.POST.get('sender')
        recipients = ['danilaitv@yandex.ru']
        send_mail(subject, message, sender, recipients)
    return render(request, 'contact.html')


def success_view(request):
    return render(request, 'about.html')
