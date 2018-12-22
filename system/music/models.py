from django.db import models

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=250)
	album_description = models.CharField(max_length=500)
	album_genre = models.CharField(max_length=250)
	publication_year= models.CharField(max_length=4)
	album_url = models.CharField(max_length=1999)


class Song(models.Model):
	#album = models.ForeignKey(Album, on_delete=models.CASCADE)
	song_title = models.CharField(max_length=250)
	file_type = models.CharField(max_length=10)
	song_url = models.CharField(max_length=1999)

class Contact(models.Model):
	full_name = models.CharField(max_length=25)
	email = models.EmailField(max_length=100)
	message = models.TextField(blank="null")
	