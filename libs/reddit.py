import praw
import os

rr: None

def init(_keys):
    global rr

    rr = praw.Reddit(
        user_agent=("IonVers 1.0 by /u/ionvers github.com/ionvers/osiris/"),
        **_keys
    )
    rr.validate_on_submit = True

def create_post(txt, title):
    global rr

    rr.subreddit('ionvers').submit(title=title,selftext=txt)

    return True
