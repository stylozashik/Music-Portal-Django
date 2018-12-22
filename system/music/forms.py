from django import forms
from .models import Album,Song,Contact

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = [
			'artist',
			'album_title',
			'album_description',
			'album_genre',
			'publication_year',
			'album_url'

		]

class SongForm(forms.ModelForm):
	class Meta:
		model = Song
		fields = [
				'song_title',
				'file_type',
				'song_url'
		]

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
				'full_name',
				'email',
				'message'
		]
