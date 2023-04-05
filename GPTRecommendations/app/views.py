"""
Definition of views.
"""

from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About GPT Music',
            'message':'GPT Music Recommendations App',
            'year':datetime.now().year,
        }
    )

def result(request):
    """Renders the result page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Result',
            'message':'GPT Recommends:',
        }
    )

def get_request(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/about/')

    else:
        form = HttpResponseRedirect('/about/')

    return HttpResponseRedirect('/about/')

def say_hello(request):
    return HTTPResponse("Hello World")