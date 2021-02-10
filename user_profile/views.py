from django.shortcuts import render

def index(request):
    data = {
        'profile_photo': 'a'
    }
    return render(request, 'main/index.html', data)

def profile(request):
    return render(request, 'main/profile.html')

def drink(request):
    return render(request, 'main/drink.html')
