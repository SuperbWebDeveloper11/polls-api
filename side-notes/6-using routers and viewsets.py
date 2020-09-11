
# using router and viewsets simplify the code 

###################### urls.py ########################

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'polls'

router = DefaultRouter() # <----
router.register('', views.PollViewSet) # <----

urlpatterns = [
    # path('', views.PollsList.as_view(), name='polls_list'), # <----
    # path('<int:pk>/', views.PollDetail.as_view(), name='poll_detail'), # <-----
    path('<int:pk>/choices/', views.ChoicesList.as_view(), name='choices_list'),
    path('<int:pk>/choices/<int:choice_pk>/vote/', views.CreateVote.as_view(), name='create_vote'),
]

urlpatterns += router.urls # <----


##################### views.py ##########################

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

'''
# retreive poll list or create poll instance
class PollsList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


# retreive poll list or create poll instance
class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
'''


class PollViewSet(viewsets.ModelViewSet): # <--------
    queryset = Poll.objects.all() # <--------
    serializer_class = PollSerializer # <--------


# retreive choices list or create choice instance
class ChoicesList(generics.ListCreateAPIView):
    def get_queryset(self):
        poll_choices = Choice.objects.filter(poll__id=self.kwargs['pk'])
        return poll_choices
    serializer_class = ChoiceSerializer


# create votes instances manually
class CreateVote(APIView):
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        new_vote = {'poll': pk, 'choice': choice_pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=new_vote)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

