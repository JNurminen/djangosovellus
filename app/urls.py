from django.urls import path
from .views import albumlistview, bandlistview, addband, addalbum, deletealbum, \
      confirmdeletealbum, deleteband, confirmdeleteband, edit_album_get, edit_album_post, \
        edit_band_get, edit_band_post, searchband, albums_filtered, \
        loginview, login_action, logout_action

urlpatterns = [
    
    # etusivu kirjautumisen jälkeen
    # path('landing/', landingview),

    # kirjautuminen
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    # albumit url
    path('albums/', albumlistview),
    path('add-album/', addalbum),
    path('delete-album/<int:id>/', deletealbum),
    path('confirm-delete-album/<int:id>/', confirmdeletealbum),
    path('edit-album-get/<int:id>/', edit_album_get),
    path('edit-album-post/<int:id>/', edit_album_post),
    path('albums-by-band/<int:id>/', albums_filtered),

    # bändit url
    path('bands/', bandlistview),
    path('add-band/', addband),
    path('delete-band/<int:id>/', deleteband),
    path('confirm-delete-band/<int:id>/', confirmdeleteband),
    path('edit-band-get/<int:id>/', edit_band_get),
    path('edit-band-post/<int:id>/', edit_band_post),
    path('search-bands/', searchband),
]