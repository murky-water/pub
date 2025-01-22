from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

import pdb

class mySerializer(serializers.json.Serializer):
    def get_dump_object(self,obj):
        return self._current

def index(request):
    context = {
        'number_of_hotels':Hotel.objects.all().count(),
        'locations_list':City.objects.all(),
    }

    return render (request, "sea/home.html", context)

def searchResponse(request):
    query=request.GET
    keyword=query.get('keyword')
    type=query.get('type')
    
    loc_list=City.objects.filter(name__icontains=keyword)
    serial = serializers.serialize('json',loc_list, fields=['name','image'])
    
    return JsonResponse(mySerializer().serialize(loc_list), safe=False)