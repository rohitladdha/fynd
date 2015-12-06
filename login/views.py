from django.shortcuts import render, render_to_response

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from login.serializers import UserSerializer, GroupSerializer


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




def test(request):
  return render_to_response('index.html')


