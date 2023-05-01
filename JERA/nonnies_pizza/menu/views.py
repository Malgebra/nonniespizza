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

def menu2(request):
    categories = Category.objects.prefetch_related('items').all()
    template = loader.get_template('menu2.html')
    context = {'categories': categories}
    return HttpResponse(template.render(context, request))