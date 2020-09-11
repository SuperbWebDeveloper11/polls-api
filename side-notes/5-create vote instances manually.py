################### urls.py ###########################
from django.urls import path, include
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.PollsList.as_view(), name='polls_list'),
    path('<int:pk>/', views.PollDetail.as_view(), name='poll_detail'),
    path('<int:pk>/choices/', views.ChoicesList.as_view(), name='choices_list'),
    path('<int:pk>/choices/<int:choice_pk>/vote/', views.CreateVote.as_view(), name='create_vote'),
]


################### views.py ###########################

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


# make post request to create vote instances:
# http POST localhost:8000/polls/1/choices/2/vote/ voted_by=1
# Note : you can not vote with the same user a second time on a specific choice
