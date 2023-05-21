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
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    """Renders the home page."""
    print("hello")
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = GPTForm(request.POST)


        #LOGIC
        query = Query(form['genre'].value(), (form['question'].value()), form['artist'].value())
        queryProcessor = QueryProcessor(query)
        QueryProcessor.process(queryProcessor)
        QueryProcessor.postRequest(queryProcessor)
        QueryProcessor.parseRequest(queryProcessor)
        if (queryProcessor.answer == "Music recommended successfully."):
          music = 'Music'
          artist = 'Artist'
        else:
            music = ''
            artist = ''
        #END OF LOGIC


        return render(
        request,
        'app/index.html',
        {
            'form': form,
            'title':'GPT Music Result',
            'entered': 'Genre: ' + form['genre'].value() + ', Question: ' + form['question'].value() + ', Artist: ' +  form['artist'].value(), 
            'sum': queryProcessor.answer,
            's1': (queryProcessor.table[0]).music,
            's2': (queryProcessor.table[0]).artist,
            's3': (queryProcessor.table[1]).music,
            's4': (queryProcessor.table[1]).artist,
            's5': (queryProcessor.table[2]).music,
            's6': (queryProcessor.table[2]).artist,
            's7': (queryProcessor.table[3]).music,
            's8': (queryProcessor.table[3]).artist,
            's9': (queryProcessor.table[4]).music,
            's10': (queryProcessor.table[4]).artist,
            's11': (queryProcessor.table[5]).music,
            's12': (queryProcessor.table[5]).artist,
            's13': (queryProcessor.table[6]).music,
            's14': (queryProcessor.table[6]).artist,
            's15': (queryProcessor.table[7]).music,
            's16': (queryProcessor.table[7]).artist,
            's17': (queryProcessor.table[8]).music,
            's18': (queryProcessor.table[8]).artist,
            'year':datetime.now().year,
            'Music': music,
            'Artist': artist,
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
def say_hello(request):
    return HttpResponseRedirect('/about/')