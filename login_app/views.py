from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from login_app.serializers import UserSerializer, GroupSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import json


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

@login_required
def sample_view(request):
  print "in sample_view"
  resp_hash = {"status": "in sample view"}
  return HttpResponse(json.dumps(resp_hash), content_type="application/json")


@csrf_exempt
def login_view(request):
  # import ipdb
  # ipdb.set_trace()
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