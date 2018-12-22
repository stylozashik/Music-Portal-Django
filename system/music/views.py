from django.shortcuts import render
from django.views.generic import FormView
from .forms import AlbumForm,SongForm,ContactForm
from django.http import HttpResponse
from .models import Album,Song,Contact

def home(request,*args,**kwargs):
	obj = Album.objects.all()
	context={

		'items' : obj
	}

	return render(request,"home.html",context)



def songs(request,*args,**kwargs):
	songs = Song.objects.all()
	context={
		'objective' : songs
	}
	return render(request,"songs.html",context)


def create(request,*args,**kwargs):
	form = AlbumForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = AlbumForm()

	context = {
		'form' : form
	}

	return render(request,"add_album.html",context)

def contact_form(request,*args,**kwargs):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ContactForm()

	context = {
		'form' : form
	}

	return render(request,"contact.html",context)


def add_song(request,*args,**kwargs):
	form = SongForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = SongForm()

	context = {
		'form' : form
	}

	return render(request,"add_song.html",context)


