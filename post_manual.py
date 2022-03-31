from libs.app import init_app, create_post


init_app()


with open('manual_posts.txt', 'r+') as fh:

    lines = []
    for line in fh:
        if line == '---':
            # post to reddit

            title = lines.pop(0)
            pst = '\n'.join(lines)

            if create_post(title, pst):
                fh.truncate(0)

            lines.clear()
        else:
            lines.append(line)
