from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import ClickerUsercounter
from django.http import HttpResponse

def clicker_view(request):
    return render(request, 'clicker/clicker_home.html')

@login_required
def update_counter(request):
    if request.method == 'POST':
        user = request.user
        user_counter, created = ClickerUsercounter.objects.get_or_create(user=user)
        
        if created:
            user_counter.counter = 0
            
        user_counter.counter += 1
        user_counter.save()
        return JsonResponse({'counter': user_counter.counter})


@login_required
def home(request):
    user = request.user
    user_counter, created = ClickerUsercounter.objects.get_or_create(user=user)
    if created:
        user_counter.counter = 0
        user_counter.save()
    return render(request, 'home.html', {'counter': user_counter.counter})

def clicker_js(request):
    content = open('path/to/your/clicker.js', 'r').read()  # Replace 'path/to/your/clicker.js' with the actual path to your JavaScript file
    return HttpResponse(content, content_type='application/javascript')