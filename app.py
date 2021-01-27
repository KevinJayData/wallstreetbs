import praw
import data_cleaning
import pandas as pd
import config
import os
import send_email


def execute():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Connect to reddit
    reddit = praw.Reddit(client_id=config.client_id,
                         client_secret=config.client_secret,
                         password=config.password,
                         user_agent=config.user_agent,
                         username=config.username)
    # Pick subreddit
    subreddit = reddit.subreddit("wallstreetbets")
    # Grab data
    df = data_cleaning.DataCleaning.run_data_cleaning(subreddit, dir_path, limit_num=100)

    df.to_csv('todays_bullshit.csv', index=False)

    send_email.send_email(config)

    os.remove("todays_bullshit.csv")


if __name__ == '__main__':
    execute()