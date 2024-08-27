from django.urls import path
from .views import landingview, albumlistview, bandlistview, addband, addalbum

urlpatterns = [
    path('', landingview),

    # albumlistview url
    path('albums/', albumlistview),
    path('add-album/', addalbum),

    # bandlistview url
    path('bands/', bandlistview),
    path('add-band/', addband),
]