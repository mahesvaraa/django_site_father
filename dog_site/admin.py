from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from multiupload.fields import MultiFileField

from .models import Carousel, CarouselImage, PhotoGallery, PhotoGalleryImage
from .models import Dog
from .models import Post


class DogForm(forms.ModelForm):
    photos = MultiFileField(min_num=1, max_num=5)

    class Meta:
        model = Dog
        fields = ['title', 'short_description', 'description', 'photo', 'slug']


# Register your models here.
class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


class DogAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Dog
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    save_as = True
    list_display = ('id', 'title', 'slug', 'description', 'get_photo', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'get_photo')
    fields = ('title', 'slug', 'description', 'photo', 'get_photo', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"> ')
        return '-'

    get_photo.short_description = 'Фото'


# class DogImageInline(admin.TabularInline):
#     model = DogImage
#     extra = 3

class DogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = DogAdminForm
    save_as = True
    list_display = ('id', 'title', 'slug', 'short_description', 'description', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('get_photo',)
    fields = ('title', 'slug', 'short_description', 'description', 'photo', 'get_photo')

    #    inlines = [DogImageInline]

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"> ')
        return '-'


class CarouselImageInline(admin.TabularInline):
    model = CarouselImage
    extra = 3


class CarouselAdmin(admin.ModelAdmin):
    inlines = [CarouselImageInline]


class PhotoGalleryImageInline(admin.TabularInline):
    model = PhotoGalleryImage
    extra = 3


class PhotoGalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoGalleryImageInline]


class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'processed', 'read')
    list_filter = ('mailbox', 'processed', 'read')


# admin.site.register(Message, MessageAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(CarouselImage)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(PhotoGalleryImage)
admin.site.register(Dog, DogAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(DogImage)
