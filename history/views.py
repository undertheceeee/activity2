from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Tweet


def all_tweets_view(request):
    """
    Renders a page displaying all tweets from all users.
    """
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'history_app/all_tweets.html', {'tweets': tweets})


def create_tweet_view(request):
    """
    Handles both displaying the tweet creation form (GET) and
    processing the form submission (POST).
    """
    if request.method == 'POST':
        # Assuming you have a logged-in user.
        # For this example, we'll use a placeholder or the first user.
        # In a real app, you would use: user = request.user
        try:
            # For demonstration, use the first user in the database
            user = User.objects.first()
            if not user:
                # Or create a user if none exist
                user = User.objects.create_user(username='testuser', password='testpassword')
        except Exception:
            # Handle cases where the User model is not available
            return redirect('all_tweets')

        content = request.POST.get('content')
        if content:
            Tweet.objects.create(content=content, user=user)
            # Redirect to the main tweets page after a successful tweet
            return redirect('all-tweets')

    # For a GET request, just render the form.
    return render(request, 'history_app/create_tweet.html')

def history_view(request):
    history = History.objects.filter(user=request.user).order_by('-date')
    return render(request, 'history/history.html', {'history': history})

