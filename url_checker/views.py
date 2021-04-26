from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def check_url(request):
  try: 
    url_status = urllib.request.urlopen(request.body.decode("utf-8")).getcode()
  except:
    return HttpResponse(": URL not working")
  if (url_status== 200):
    return HttpResponse("Yes! URL works!")
  return HttpResponse(": URL not working")