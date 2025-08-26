from django.urls import path
from . import views

urlpatterns = [
    path('tweets/', views.all_tweets_view, name='all_tweets'),
    path('tweets/create/', views.create_tweet_view(), name='tweet_creation_button'),
    path('', history_view, name='user-history'),
]