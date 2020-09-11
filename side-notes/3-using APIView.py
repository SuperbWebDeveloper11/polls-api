################### urls.py #########################
from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.PollsList.as_view(), name='polls_list'),
    path('<int:pk>/', views.PollDetail.as_view(), name='poll_detail'),
]


################### views.py #########################
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import Poll, Choice, Vote
from .serializers import PollSerializer

# return polls list 
class PollsList(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        data = PollSerializer(polls, many=True).data
        return Response(data)


# return poll detail 
class PollDetail(APIView):
    def get(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        data = PollSerializer(poll).data
        return Response(data)

# also try to make an options request
## http OPTIONS localhost:8000/polls/
## http OPTIONS localhost:8000/polls/2/

# the response is something like this:
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 169
Content-Type: application/json
Date: Fri, 11 Sep 2020 14:06:28 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.6.9
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "description": "",
    "name": "Polls List",
    "parses" [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
        ],
    "renders" [
        "application/json",
        "text/html"
        ]
    }
}

