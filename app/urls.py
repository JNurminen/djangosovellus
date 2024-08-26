from django.urls import path
from .views import landingview, albumlistview, bandlistview

urlpatterns = [
    path('', landingview),

    # albumlistview url
    path('albums/', albumlistview),

    # bandlistview url
    path('bands/', bandlistview),
]