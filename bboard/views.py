from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Bb


# Create your views here.
def home(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {
        'bbs': bbs,
    }
    return HttpResponse(template.render(context, request))
