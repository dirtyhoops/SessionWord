from django.shortcuts import render, redirect
from time import strftime
import time

# Create your views here.

def index(request):
    if 'word' not in request.session:
        request.session['word'] = ''
    if 'listclass' not in request.session:
        request.session['listclass'] = ''
    if 'fontsize' not in request.session:
        request.session['fontsize'] = ''
    if 'listofwords' not in request.session:
        request.session['listofwords'] = []

    style = {
        "listofwords": request.session['listofwords']
    }
    
    return render(request, 'first_app/index.html', style)

def add(request):
    if request.method == 'POST':
        request.session['word'] = request.POST['word']
        color = request.POST['color']
        times = strftime("%X %p, %B %d %Y")
        timestamp = "- added on " + times

        if color == "red" and 'fontsize' in request.POST:
            word = "<li class = 'redlistBig'>" + request.session['word'] + "</li>"
        elif color == "green" and 'fontsize' in request.POST:
            word = "<li class = 'greenlistBig'>" + request.session['word'] + "</li>"
        elif color == "blue" and 'fontsize' in request.POST:
            word = "<li class = 'bluelistBig'>" + request.session['word'] + "</li>"
        elif color == "red" and 'fontsize' not in request.POST:
            word = "<li class = 'redlist'>" + request.session['word'] + "</li>"
        elif color == "green" and 'fontsize' not in request.POST:
            word = "<li class = 'greenlist'>" + request.session['word'] + "</li>"
        elif color == "blue" and 'fontsize' not in request.POST:
            word = "<li class = 'bluelist'>" + request.session['word'] + "</li>"

        request.session['listofwords'].append(word + timestamp)
    
        
        


    return redirect('/')


def clear(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('/')
