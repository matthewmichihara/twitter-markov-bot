import markovify
import os
import tweepy
import yaml
from tweet_fetcher import TweetFetcher
from twitter_bot import TwitterBot


class Factory:
    def config(self):
        path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        config = yaml.safe_load(open(path).read())
        return config

    def twitter_api(self, config):
        auth = tweepy.OAuthHandler(config['API_KEY'], config['API_SECRET'])
        auth.set_access_token(config['ACCESS_TOKEN'], config['ACCESS_TOKEN_SECRET'])
        api = tweepy.API(auth)
        return api
        
    def fetcher(self, twitter_api):
        fetcher = TweetFetcher(twitter_api)
        return fetcher

    def twitter_user(self, config):
        return config['TWITTER_USER']
        
    def model(self, fetcher, twitter_user):
        tweet_texts = fetcher.fetch(twitter_user)
        joined = '\n'.join(tweet_texts)
        model = markovify.NewlineText(joined)
        return model

    def bot(self):
        config = self.config()
        twitter_api = self.twitter_api(config)
        fetcher = self.fetcher(twitter_api)
        twitter_user = self.twitter_user(config)
        model = self.model(fetcher, twitter_user)
        bot = TwitterBot(twitter_api, model)
        return bot
