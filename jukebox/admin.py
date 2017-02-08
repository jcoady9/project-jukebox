from django.contrib import admin
from django import forms
from .models import Album, Track

# Register your models here.

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class TrackInline(admin.StackedInline):
    model = Track
    extra = 0

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist']
    inlines = [TrackInline,]
    form = AlbumForm

admin.site.register(Track)
admin.site.register(Album, AlbumAdmin)
