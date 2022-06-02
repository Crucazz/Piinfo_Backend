from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView

import core.models as models
import core.serializers as serials
@csrf_exempt
def aPage(request):
    user:User=User.objects.get(pk=1)
    username =request.POST.get("UserName")
    email =request.POST.get("email")
    return JsonResponse({"UserName":username,"email":email})

@csrf_exempt
@api_view(['GET', 'DELETE'])
def PymeListView(request):
    queryset = models.Pyme.objects.all()
    serializer_class= serials.PymeSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)

@csrf_exempt
@api_view(['GET', 'DELETE'])
def PropagandaListView(request):
    queryset = models.Propaganda.objects.all()
    serializer_class= serials.PropagandaSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)