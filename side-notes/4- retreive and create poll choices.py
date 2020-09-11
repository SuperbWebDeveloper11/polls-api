################## urls.py ##################
from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.PollsList.as_view(), name='polls_list'),
    path('<int:pk>/', views.PollDetail.as_view(), name='poll_detail'),
    path('<int:pk>/choices/', views.ChoicesList.as_view(), name='choices_list'),
]

################## view.py ##################

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework import generics 
from rest_framework.response import Response
from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer

# retreive poll list or create poll instance
class PollsList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


# retreive poll list or create poll instance
class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


# retreive choices list or create choice instance
class ChoicesList(generics.ListCreateAPIView):
    def get_queryset(self):
        poll_choices = Choice.objects.filter(poll__id=self.kwargs['pk'])
        return poll_choices
    serializer_class = ChoiceSerializer

# retreive choices :
# http localhost:8000/polls/1/ 

# create a choice :
# http POST localhost:8000/polls/1/ choice_text='something else' poll=1
