from django.shortcuts import render

def clicker_view(request):
    return render(request, 'clicker/clicker_home.html')