from django.urls import path
from .views import landingview, albumlistview, bandlistview, addband, addalbum, deletealbum, \
      confirmdeletealbum, deleteband, confirmdeleteband

urlpatterns = [
    path('', landingview),

    # albumlistview url
    path('albums/', albumlistview),
    path('add-album/', addalbum),
    path('delete-album/<int:id>/', deletealbum),
    path('confirm-delete-album/<int:id>/', confirmdeletealbum),

    # bandlistview url
    path('bands/', bandlistview),
    path('add-band/', addband),
    path('delete-band/<int:id>/', deleteband),
    path('confirm-delete-band/<int:id>/', confirmdeleteband),
]