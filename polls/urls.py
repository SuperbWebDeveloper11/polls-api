from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.PollsList.as_view(), name='polls_list'),
    path('<int:pk>/', views.PollDetail.as_view(), name='poll_detail'),
    path('<int:pk>/choices/', views.ChoicesList.as_view(), name='choices_list'),
    path('<int:pk>/choices/<int:choice_pk>/vote/', views.CreateVote.as_view(), name='create_vote'),
]
