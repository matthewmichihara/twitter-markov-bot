class TwitterBot:
    def __init__(self, twitter_api, model):
        self.api = twitter_api
        self.model = model

    def tweet(self):
        tweet_text = self.model.make_short_sentence(140)
        if tweet_text:
            self.api.update_status(tweet_text)
        return tweet_text
