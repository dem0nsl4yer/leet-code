import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame({'tweet_id': tweets['tweet_id'][tweets['content'].str.len() >15]})
    return result