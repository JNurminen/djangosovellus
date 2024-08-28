from django.shortcuts import render, redirect
from .models import Band, Album

# Luodaan näkymät

def landingview(request):
    return render(request, 'landingpage.html')

# album näkymä
def albumlistview(request):
    albumlist = Album.objects.all()
    bandlist = Band.objects.all()
    context = {'albums': albumlist, 'band': bandlist}
    return render(request, "albumlist.html", context)

# albumin lisäys näkymä
def addalbum(request):
    a = request.POST['name']
    b = request.POST['band']
    c = request.POST['year']
    Album(name=a, band=Band.objects.get(id=b), year=c).save()
    return redirect(request.META['HTTP_REFERER'])

# poista albumi
def confirmdeletealbum(request, id):
    album = Album.objects.get(id=id)
    context = {'album': album}
    return render(request, 'confirmdelalb.html', context)

def deletealbum(request, id):
    Album.objects.get(id=id).delete()
    return redirect(albumlistview)



# bändi näkymä
def bandlistview(request):
    bandlist = Band.objects.all()
    context = {'bands': bandlist}
    return render(request, "bandlist.html", context)

# bändin lisäys näkymä
def addband(request):
    a = request.POST['name']
    b = request.POST['country']
    c = request.POST['genre']
    d = request.POST['year']
    Band(name=a, country=b, genre=c, year=d).save()
    return redirect(request.META['HTTP_REFERER'])

# poista bändi
def confirmdeleteband(request, id):
    band = Band.objects.get(id=id)
    context = {'band': band}
    return render(request, 'confirmdelband.html', context)

def deleteband(request, id):
    Band.objects.get(id=id).delete()
    return redirect(bandlistview)
