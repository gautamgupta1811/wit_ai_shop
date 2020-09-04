from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from wit_files import wit_speech


# Create your views here.

def home(request):
    return render(request, 'index.html')

def mic(request):
    text = wit_speech.RecognizeSpeech('myspeech.wav', 4)
    print(text)
    return redirect(reverse('home')+ '#deal-href')

def section_id():
    return '#deal-href'