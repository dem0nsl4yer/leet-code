import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame({'tweet_id': tweets['tweet_id'][tweets['content'].str.len() >15]})
    return result


## solution 2:

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df =  tweets[tweets['content'].str.len() >15]
    return df[['tweet_id']]

## solution 3: 

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['length'] = [tweets['content'].str.len()
    return tweets[tweets['length']>15]['tweet_id'].to_frame()