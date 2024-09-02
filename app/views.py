from django.shortcuts import render, redirect
from .models import Band, Album
from django.contrib.auth import authenticate, login, logout

# Luodaan näkymät

# etusivu
'''
def landingview(request):
    return render(request, 'landingpage.html')
    '''

# kirjautumisnäkymä
def loginview(request):
    return render(request, 'loginpage.html')

# rekisteröintinäkymä
def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')

# kirjautumisen lopetus
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

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

# muokkaa albumia
def edit_album_get(request, id):
    album = Album.objects.get(id=id)
    context = {'album': album}
    return render(request, 'edit_album.html', context)

def edit_album_post(request, id):
    album = Album.objects.get(id=id)
    album.name = request.POST['name']
    album.year = request.POST['year']
    album.save()
    return redirect(albumlistview)

# etsi albumi
def albums_filtered(request, id):
    albumlist = Album.objects.all()
    filteredalbums = albumlist.filter(band=id)
    context = {'albums': filteredalbums}
    return render(request, "albumlist.html", context)



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

# etsi bändi
def searchband(request):
    search = request.POST['search']
    filtered = Band.objects.filter(name__icontains=search)
    context = {'bands': filtered}
    return render(request, "bandlist.html", context)

# poista bändi
def confirmdeleteband(request, id):
    band = Band.objects.get(id=id)
    context = {'band': band}
    return render(request, 'confirmdelband.html', context)

def deleteband(request, id):
    Band.objects.get(id=id).delete()
    return redirect(bandlistview)

# muokkaa bändiä
def edit_band_get(request, id):
    band = Band.objects.get(id=id)
    context = {'band': band}
    return render(request, 'edit_band.html', context)

def edit_band_post(request, id):
    band = Band.objects.get(id=id)
    band.country = request.POST['country']
    band.genre = request.POST['genre']
    band.year = request.POST['year']
    band.save()
    return redirect(bandlistview)
