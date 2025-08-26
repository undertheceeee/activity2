from django.urls import path
from .views import create_tweet, tweet_success
from . import views
from .views import create_tweet, all_tweets_view


app_name = 'tweets'
urlpatterns = [
    path('create/', create_tweet, name='create_tweet'),
    path('success/', tweet_success, name='tweet_success'),
    path('create/', views.create_tweet, name='create'),
    path('', views.all_tweets_view, name='all-tweets'),
    path('create/', views.tweet_view, name='create_tweet'),
    path('', views.tweet_list, name='list'),
    path('', all_tweets_view, name='all-tweets'),
    path('', views.tweet_list, name='list'),
    path('create/', views.create_tweet, name='create'),
    path('create/', create_tweet, name='create_tweet'),
    path('', all_tweets_view, name='all-tweets'),



]