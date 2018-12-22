from django.contrib import admin
from .models import Album,Contact,Song

admin.site.site_header = 'Admin Dashboard'
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Contact)