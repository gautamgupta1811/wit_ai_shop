from django.shortcuts import render
from django.http import HttpResponse
from wit_files import wit_speech


# Create your views here.

def home(request):
    return render(request, 'index.html')

def mic(request):
    text = wit_speech.RecognizeSpeech('myspeech.wav', 4)
    print(text)
    return HttpResponse(text)
