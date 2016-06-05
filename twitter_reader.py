import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os

import pyttsx

CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'

class BotStreamListener(StreamListener):

    def __init__(self):
        super(BotStreamListener, self).__init__()
        self.engine = pyttsx.init()
        self.engine.startLoop(False)
    
    def on_status(self, status):
        if status.text == '#EXIT':
            self.engine.endLoop()
        print status.text
        self.engine.say(status.text)
        self.engine.iterate()

    def on_error(self, status):
        print status


if __name__ == '__main__':
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    myStream = Stream(auth, listener=BotStreamListener())
    myStream.filter(follow=['TWITTER_USER_ID'])
    # myStream.filter(track=['KEYWORD'])
