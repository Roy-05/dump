import praw
from praw.models import MoreComments

CLIENT_ID = 'CLIENT_ID'
CLIENT_SECRET = 'CLIENT_SECRET'
username = 'username'
password = 'password'
threadID = '...' #ID of the comments thread to parse

reddit = praw.Reddit(user_agent='Comment Extraction',
                    client_id = CLIENT_ID, 
                    client_secret = CLIENT_SECRET,
                    username = username,
                    password = password)

submissions = reddit.submission(id=threadID) 
submissions.comments.replace_more(limit=None)

f = open("reddit_comments.txt", "w+")
for comments in submissions.comments.list(): 
    f.write(comments.body)

f.close()