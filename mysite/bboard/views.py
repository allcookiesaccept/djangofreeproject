from django.http import HttpResponse
from .models import Bb
from django.template import loader
from django.shortcuts import render

def index(request):
    bbs = Bb.objects.order_by('-published')

    return render(request, 'bboard/bboard_index.html', {'bbs': bbs})
