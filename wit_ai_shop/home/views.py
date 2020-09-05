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
    id_list = ['new_products_id','laptops_id','mobiles_id','header_id','cameras_id','cart_id', 'special_deal_id']
    try:
        entity = text['entities']
        section = entity['scroll_section:scroll_section'][0]
        id_ref = section['value']
        if id_ref in id_list:
            final_id = "#" + id_ref
            return redirect(reverse('home')+ final_id)
        else:
            return redirect(reverse('home')+'#kuchbhi')
    except:
        return redirect(reverse('home')+'#kuchbhi')
