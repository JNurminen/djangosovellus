# Jos rekisteröit mallisi tänne, voit hallita niitä admin-sivulla.

from django.contrib import admin
from app.models import Band, Album

# Rekisteröi Band ja Album -mallit admin-sivulla

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass