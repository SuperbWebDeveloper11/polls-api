from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'polls'

router = DefaultRouter()
router.register('', views.PollViewSet)

urlpatterns = [
    # path('', views.PollsList.as_view(), name='polls_list'),
    # path('<int:pk>/', views.PollDetail.as_view(), name='poll_detail'),
    path('<int:pk>/choices/', views.ChoicesList.as_view(), name='choices_list'),
    path('<int:pk>/choices/<int:choice_pk>/vote/', views.CreateVote.as_view(), name='create_vote'),

    # create new user
    path('users/', views.UserCreate.as_view(), name='create_user'),
    # login
    path("login/", views.LoginView.as_view(), name="login"),
]

urlpatterns += router.urls

