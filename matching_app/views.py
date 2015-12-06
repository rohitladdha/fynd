from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from matching_engine import Preferences
from matching_engine import MatchingEngine

import json

@login_required(login_url='/auth/login')
def get_intersection(request):
  # if request.user.is_authenticated():
  try:
    params = request.GET
    prefs = []
    size = int(params.get('size',''))
    for count in range(1, size+1):
      lat = float(params.get('lat'+str(count), ''))
      lon = float(params.get('lon'+str(count), ''))
      range_value = int(params.get('range'+str(count), ''))
      range_type = params.get('range_type'+str(count), '')
      prefs.append(Preferences(lat, lon, range_value, range_type))

    matching_engine = MatchingEngine()
    suggestions = matching_engine.get_suggestions(prefs)
    return HttpResponse(json.dumps(suggestions), content_type="application/json")
  except IndexError: 
    return HttpResponseBadRequest(json.dumps({"status": "Bad request"}), content_type="application/json")
  except Exception as e: 
    return HttpResponseForbidden(json.dumps({"status": "Unprocessable request"}), content_type="application/json")
