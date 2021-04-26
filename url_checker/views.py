from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.conf import settings

import urllib.request
import logging
import os
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

class FrontendAppView(View):
  def get(self, request):
    print(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html'))
    try:
      with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
        return HttpResponse(f.read())
    except FileNotFoundError:
      logging.exception('Production build of app not found')
      return HttpResponse(status=501)