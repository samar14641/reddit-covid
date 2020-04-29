import datetime
import os
import pandas as pd
import praw
from dotenv import load_dotenv


commentsReqd = False
load_dotenv()

def setup():
    # read the env file
    appName = os.getenv('APP_NAME')
    clientID = os.getenv('CLIENT_ID')
    clientSecret = os.getenv('CLIENT_SECRET')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')

    # create the PRAW instance
    reddit = praw.Reddit(
        client_id = clientID, 
        client_secret = clientSecret, 
        user_agent = appName,
        username = user,
        password = password
    )

    return reddit

def getSubData():
    reddit = setup()
    subreddit = reddit.subreddit('Coronavirus')

    count = 1
    limit = 400 if commentsReqd else 1000
    posts = {}

    for submission in subreddit.top('all', limit = limit):
        # print('THREAD', count)

        posts[submission.id] = {
            'title': submission.title, 
            'url': submission.url, 
            'selftext': submission.selftext,
            'score': submission.score,
            'ups': submission.ups,
            'downs': submission.downs,
            'permalink': submission.permalink,
            'created': datetime.datetime.fromtimestamp(submission.created),  # convert UNIX timestamp
            'numComm': submission.num_comments,
            'topLevelComments': []
        }

        count += 1

    if commentsReqd:
        df = pd.DataFrame(posts).T

        getTopLevelComments(reddit, df)

    else:
        df = pd.DataFrame(posts)
        df.to_json(os.getcwd() + '\\data.json', date_format = 'iso')  # override epoch format

        df = df.T
        df.to_csv(os.getcwd() + '\\data.csv')


def getTopLevelComments(reddit, df):
    count = 1

    for postID in df.index:  # get top level comments for each thread using id
        # print('COMMENT', count)

        submission = reddit.submission(id = postID)

        submission.comments.replace_more(limit = 0)  # remove MoreComments objects from the comment tree

        for comment in submission.comments:
            df.loc[postID, 'topLevelComments'].append({'comID': comment.id, 'comText': comment.body})  # store comment id and text

        count += 1

    df.to_csv(os.getcwd() + '\\data_comments_large.csv')

    df = df.T
    df.to_json(os.getcwd() + '\\data_comments_large.json', date_format = 'iso')  # override epoch format

def main():
    print('Getting comments:', commentsReqd)
    getSubData()

main()