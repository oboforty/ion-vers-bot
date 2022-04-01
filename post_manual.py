import os
from libs.app import init_app, create_post, close_app


init_app()

FILTERED = False

with open('manual_posts.txt', 'r', encoding='utf-8') as fh:
    for line in fh:
        try:
            create_post(line, FILTERED)
        except Exception as e:
            print("ERROR: ")
            print(e)
            print(line)
            print("------------------------------------------------------------------------")

    #fh.truncate(0)

close_app()
os.remove("manual_posts.txt")
