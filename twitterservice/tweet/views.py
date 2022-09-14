from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.utils.safestring import mark_safe
import tweepy

def connectTwitter():
    """connects to the twitter api and returns the client object"""
    
    try:    
        client = tweepy.Client(
            consumer_key=settings.API_KEY,
            consumer_secret=settings.API_KEY_SECRET,
            access_token=settings.ACCESS_TOKEN,
            access_token_secret=settings.ACCESS_TOKEN_SECRET
        )
        return client
    except Exception as err:
        print(err)

# creates a tweet from content tweet_text and returns the tweet id
def create_tweet(tweet_text):
    """Creates a tweet from tweet content and returns the tweet id for the created tweet and a message for the gui"""
    client = connectTwitter()
    try:
        tweet = client.create_tweet(text=tweet_text, user_auth=True)
        message = 'tweet sent'
        tweet_id = tweet[0].get('id')
        print(f"created tweet: {tweet_text}")
        return tweet_id, tweet_text
    except Exception as e:
        message = "failed to send"
        tweet_id = None
        print(e)
        return tweet_id, message

def delete_tweet(tweet_id):
    """Deletes a tweet from tweet text and returns a message for the gui"""
    client = connectTwitter()
    try:
        client.delete_tweet(id=tweet_id, user_auth=True)
        message = "tweet deleted"
        return message
    except:
        message = 'failed to delete'
        return message

def retrieve_tweet(twitter_handle):
    client = connectTwitter()
    try:
        user = client.get_user(username=twitter_handle, user_auth=True)
        user_id = user[0].id
        print(user_id)
        tweets=client.get_users_tweets(user_id, user_auth=True,max_results=100)
        print(tweets)
        results=[]
        for tweet in tweets[0]:
            results.append(tweet.text)
        return results
    except:
        message = 'retrieve failed'
        return message

def index(request):
    print(request.method)
    if request.method == 'POST':
        content = request.POST.get('content','')
        twitter_handle= request.POST.get('twitter_handle','')
        delete=request.POST.get('delete_id','')
        if content:
            print ('Content:', content)
            tweet_id, message=create_tweet(content)
            messages.success(request,'twitter link : https://twitter.com/sirishacyd/status/'+tweet_id+' Message: '+message)
            return render(request, 'tweet/index.html')
        elif twitter_handle:
            print ('Twitter Handle:', twitter_handle)
            results=retrieve_tweet(twitter_handle)
            # print(results)
            messages.success(request,'End of Timeline')
            return render(request, 'tweet/index.html',{'public_tweets':results})
        elif delete:
            print ('delete_id:', delete)
            message=delete_tweet(delete)
            messages.success(request,'tweet with id deleted : '+delete)
            return render(request, 'tweet/index.html')
    return render(request,'tweet/index.html')