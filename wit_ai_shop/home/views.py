from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from wit_files import wit_speech
import json

# Create your views here.

def home(request):
    return render(request, 'index.html')       

def mic(request):
    text = wit_speech.RecognizeSpeech('myspeech.wav', 4)
    print(text)
    id_href = '#deal-href'
    return redirect(reverse('home')+ id_href)
