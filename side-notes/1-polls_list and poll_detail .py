# returning polls list and poll detail manually using functional based views

################### urls.py ################### 
from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.polls_list, name='polls_list'),
    path('<int:pk>/', views.poll_detail, name='polls_detail'),
]



################### views.py ################### 
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Poll, Choice, Vote

# return polls_list manually
def polls_list(request):
    polls = Poll.objects.all()
    polls_list = list(polls.values('question', 'pub_date', 'created_by__username'))
    data = { 'results': polls_list }
    return JsonResponse(data)


# return poll_detail manually
def poll_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = { 'results': {
        'question': poll.question,
        'pub_date': poll.pub_date,
        'created_by__username': poll.created_by.username,
        }}
    return JsonResponse(data)
