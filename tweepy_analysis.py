from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = "fasdffasdf"
consumer_secret = "fasdffasdf"
access_token = "fasdffasdf"
access_secret = "fasdffasdf"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(data)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track = ["python"])
