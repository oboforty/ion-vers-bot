from libs.app import init_app, create_post


init_app()


with open('manual_posts.txt', 'r+', encoding='utf-8') as fh:

    for line in fh:
        create_post(line)

    #fh.truncate(0)
