from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from wit_files import wit_speech
import json

# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')       

def mic(request):
    text = wit_speech.RecognizeSpeech('myspeech.wav', 4)
    print(text)
    if request.method == 'POST':
        data = json.dumps({'id':'#deal-href'})
        return render(request, 'index.html', {'data':data})

