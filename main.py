from factory import Factory
import os
import random
import tweepy
import webapp2
import yaml


class TweetHandler(webapp2.RequestHandler):
    def get(self):
        bot = Factory().bot()
        msg = bot.tweet()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(msg)

app = webapp2.WSGIApplication([
    ('/tasks/tweet', TweetHandler)
], debug=True)
