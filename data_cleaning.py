import pandas as pd
from string import punctuation
from datetime import datetime

class DataCleaning(object):

    @classmethod
    def run_data_cleaning(cls, subreddit, dir_path, limit_num):
        df = cls.grab_data(subreddit, limit_num)
        df = cls.create_comment_ticker_sets(df, dir_path)
        df = cls.sort_df(df)
        df = cls.prep_email_df(df)
        return df

    @classmethod
    def grab_data(cls, subreddit, limit_num):
        submission_info = []
        count = 1
        for submission in subreddit.new(limit=limit_num):
            print('title {}: {}'.format(count, submission.title))
            count += 1
            # submission.comments.replace_more(limit=0)
            # for comment in submission.comments.list():
            submission.comments.replace_more(limit=None)
            comment_queue = submission.comments[:]  # Seed with top-level
            while comment_queue:
                comment = comment_queue.pop(0)
                comment_queue.extend(comment.replies)
                submission_info.append({'title': submission.title,
                                        'score': submission.score,
                                        'submission_url': submission.url,
                                        'title_created_utc': pd.to_datetime(datetime.fromtimestamp(submission.created_utc)),
                                        'comment': comment.body.translate(str.maketrans('', '', punctuation)),
                                        'comment_score': comment.score,
                                        'comment_permalink': comment.permalink,
                                        'comment_created_utc': pd.to_datetime(datetime.fromtimestamp(comment.created_utc))})

        submission_df = pd.DataFrame(submission_info)
        return submission_df

    @classmethod
    def create_comment_ticker_sets(cls, df, dir_path):
        # Get stock tickers
        stocks = pd.read_csv(dir_path + '/stocks.csv')
        stocks_set = set(stocks['ACT Symbol'])

        # since the grain is at the comment level, expand grain to the mention level.
        # grab comment url and then merge on that?

        mention_grain_list = []
        for i in range(len(df)):
            mention_grain_list.append(list(stocks_set.intersection(set((df['comment'][i]).split(' ')))))
        df['ticker'] = mention_grain_list

        # Remove comments without matches
        # df = df[df['ticker'].map(len) >0]
        match_grain = []
        for i in range(len(df)):
            if len(df['ticker'][i])==1:
                match_grain.append({'title': df['title'][i],
                                    'score': df['score'][i],
                                    'submission_url': df['submission_url'][i],
                                    'comment': df['comment'][i],
                                    'comment_score': df['comment_score'][i],
                                    'ticker': df['ticker'][i],
                                    'title_created_utc': pd.to_datetime(df['title_created_utc'][i]),
                                    'comment_created_utc': pd.to_datetime(df['comment_created_utc'][i]),
                                    'comment_permalink': df['comment_permalink'][i]
                                    })
            elif len(df['ticker'][i])>=1:
                for j in df['ticker'][i]:
                    match_grain.append({'title': df['title'][i],
                                        'score': df['score'][i],
                                        'submission_url': df['submission_url'][i],
                                        'comment': df['comment'][i],
                                        'comment_score': df['comment_score'][i],
                                        'ticker': [j],
                                        'title_created_utc': pd.to_datetime(df['title_created_utc'][i]),
                                        'comment_created_utc': pd.to_datetime(df['comment_created_utc'][i]),
                                        'comment_permalink': df['comment_permalink'][i]
                                        })
            else:
                pass
        new_df = pd.DataFrame(match_grain)
        new_df['ticker'] = new_df['ticker'].apply(lambda row: ''.join(row))
        # Get the total count for each ticker
        ticker_counts = new_df.groupby(['ticker']).size().to_frame()
        # left join the ticker count into the larger dataframe
        new_df = pd.merge(new_df, ticker_counts, 'left', on='ticker')
        new_df.rename(columns={0: 'ticker_count'}, inplace=True)
        return new_df

    @classmethod
    def sort_df(cls, df):
        df.sort_values(['ticker_count'], ascending=[False], inplace=True)
        df['rank'] = df.groupby(by=['ticker'])['comment_score'].transform(lambda x: x.rank(ascending=False))
        return df

    @classmethod
    def prep_email_df(cls, df):
        email_df = df[df['rank']==1]
        email_df = email_df[['ticker', 'ticker_count', 'comment', 'comment_created_utc', 'comment_score', 'comment_permalink']].head(20)
        print(email_df)
        return email_df
