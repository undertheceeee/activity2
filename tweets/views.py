from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TweetForm
from .models import Tweet

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_success')
    else:
        form = TweetForm()
    return render(request, 'tweets/create_tweet.html', {'form': form})


def tweet_success(request):
    return render(request, 'tweets/success.html')
def all_tweets_view(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/all_tweets.html', {'tweets': tweets})
def tweet_view(request):
    if request.method == 'POST':
        # Create a form instance from the submitted data
        form = TweetForm(request.POST)
        if form.is_valid():
            # Save the new tweet to the database
            form.save()
            return redirect('tweets:all_tweets')  # Redirect to the home page after saving
    else:
        # If the request is a GET, create a new, empty form
        form = TweetForm()

    # Render the template with the form
    return render(request, 'tweets/create_tweet.html', {'form': form})


def tweet_list(request):
    """
    Retrieves all tweets and displays them.
    """
    # This line retrieves all tweets from the database
    all_tweets = Tweet.objects.all().order_by('-created_at')

    # This sends the tweets to the template
    return render(request, 'tweets/tweet_list.html', {'tweets': all_tweets})


def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_success')  # or wherever you want to go
    else:
        form = TweetForm()

    return render(request, 'tweets/create_tweet.html', {'form': form})
