from django.shortcuts import render

# Luodaan näkymät

def landingview(request):
    return render(request, 'landingpage.html')

def albumlistview(request):
    return render(request, 'albumlist.html')

def bandlistview(request):
    return render(request, 'bandlist.html')
