"""
Definition of views.
"""

from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.models import Query
from app.models import QueryProcessor
from .forms import GPTForm

def home(request):
    """Renders the home page."""
    print("hello")
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = GPTForm(request.POST)


        #LOGIC
         
        #s =  int(form['genre'].value()) + int(form['question'].value())
        query = Query(form['genre'].value(), (form['question'].value()))
        queryProcessor = QueryProcessor(query)
        QueryProcessor.process(queryProcessor)
        QueryProcessor.postRequest(queryProcessor)
        s = queryProcessor.answer
        #END OF LOGIC


        return render(
        request,
        'app/index.html',
        {
            'form': form,
            'title':'GPT Music Result',
            'entered': 'Genre: ' + form['genre'].value() + ', Question: ' + form['question'].value(), 
            'sum': s,
            'year':datetime.now().year,
        })
    form = GPTForm()
    return render(
        request,
        'app/index.html',
        {
            'form': form,
            'title':'GPT Music',
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

def say_hello(request):
    return HttpResponseRedirect('/about/')