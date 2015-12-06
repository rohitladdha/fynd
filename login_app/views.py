from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.template import Context, Template

import json

@login_required(login_url='/auth/login')
def sample_view(request):
  if request.user.is_authenticated():
    resp_hash = {"status": "in sample view"}
    return HttpResponse(json.dumps(resp_hash), content_type="application/json")
  else:
    resp_hash = {'status': 'user not logged in'}
    return HttpResponseForbidden(json.dumps(resp_hash), content_type="application/json")


@csrf_exempt
def login_view(request):
  print "doing login"
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is not None:
    if user.is_active:
      login(request, user)
      print "logged in "
      resp_hash = {"status": "logged in"}
      # Redirect to a success page.
    else:
      resp_hash = {"status": "user not active"}

      print "user is not active"
      # Return a 'disabled account' error message
          
  else:
    # Return an 'invalid login' error message.
     resp_hash = {"status": "invalid login"}
  return HttpResponse(json.dumps(resp_hash), content_type="application/json")

def logout_view(request):
  logout(request)
  resp_hash = {"status": "logged out"}
  return HttpResponse(json.dumps(resp_hash), content_type="application/json")

  # Redirect to a success page.