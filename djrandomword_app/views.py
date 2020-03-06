from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def randomword(request):
    b = get_random_string(length=14)
    if 'count' not in request.session:
        request.session['count'] = 0
    context = { "randomstr": b
    }
    
    return render(request, 'index.html', context)

def redirect_random(request):
    request.session['count'] += 1
    return redirect('/')

def clearcount(request):
    request.session.clear()
    return redirect('/')

    