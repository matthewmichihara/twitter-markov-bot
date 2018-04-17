import re


class TweetFetcher:
    """Fetches all tweets for a user"""
    
    def __init__(self, twitter_api):
        self.api = twitter_api

    def fetch(self, screen_name):
        all_tweets = []
        should_fetch = True

        while should_fetch:
            if not all_tweets:
                new_tweets = self.api.user_timeline(screen_name = screen_name, count = 200)
            else:
                oldest = all_tweets[-1].id - 1
                new_tweets = self.api.user_timeline(screen_name = screen_name, count = 200, max_id = oldest)

            all_tweets.extend(new_tweets)
            should_fetch = len(new_tweets) > 0

            print "Fetched {} tweets. {} total.".format(len(new_tweets), len(all_tweets))
        
        filtered_tweet_texts = self.filter_tweet_texts(all_tweets)
        num_filtered = len(all_tweets) - len(filtered_tweet_texts)
        print "Filtered out {} tweets. Total is now {}.".format(num_filtered, len(filtered_tweet_texts))

        return filtered_tweet_texts
    
    def filter_tweet_texts(self, tweets):
        texts = [tweet.text.encode("utf-8") for tweet in tweets]
        scrubbed_texts = [self.scrub_tweet_text(text) for text in texts]
        filtered_texts = [text for text in scrubbed_texts if self.is_valid_tweet_text(text)]
        return filtered_texts

    def scrub_tweet_text(self, text):
        scrubbed = re.sub(r'@\S+', '', text)
        return scrubbed.strip()

    def is_valid_tweet_text(self, text):
        blacklist = ["http"]
        for s in blacklist:
            if s in text:
                return False

        return True
        
