from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Item,Category,MENU

def menu(request):
    template = loader.get_template('menu.html')
    myitems = Item.objects.all().values()

    context = {
        'myitems': myitems,
    }
    return HttpResponse(template.render(context, request))
