import hashlib
import re

_filters = [
    "Write a comment…",
    "Write a comment",
    "Write a reply…",
    'All comments',
    'LikeCommentShare',
    # 'Like',
    # 'Likes',
    # 'Reactions',
    # 'comments',
    # 'comment',
    # 'Comment',
    'Replyreplied',
    'LikeReply',
    'LikeComment',
    'Share',
    'Edited',
    '﻿Ion Danvers',
    'Ion Danvers replied',
    'Redmond Csombordi',
    'József Mash Trencsényi',
    'Jozsef Mash Trencsenyi',
    ' w ',
    ' h ',
    ' d ',
    'Reply',
    'Replied',
    'replied'
]
_re_filters = [
    r'Share\s?\d+ commentsWrite a comment…',
    r'Share\s?\d+ comments',
    r"View\s?\d+ previous comments",
    r"\d+ comments",
    r"\d+ comment comment",
    r"\d+ comment",
    r"\d+ reply",
    r"\d+ replies",
    r"https\:\/\/.*\.com",
    r"https\:\/\/.*\.hu",
    r"https\:\/\/.*\.net",
]

def strip_digit(x):
    if len(x) < 3:
        return ""
    if x[0].isdigit():
        x = x[1:]
    if x[-1].isdigit():
        x = x[:-1]
    return x


def _post_filter(line):

    # split fb markup
    for _filter in _re_filters:
        line = re.sub(_filter, " ", line)

    for _filter in _filters:
        ss = filter(lambda x: x.strip()!="", map(strip_digit, line.split(_filter)))
        line = "".join(ss)

    if line.endswith(' w') or line.endswith(' h'):
        line = line[:-2]
    if line.endswith('...'):
        line = line[:-3]
    if line.endswith('...'):
        line = line[:-3]
    return line


def preprocess(line):
    #_md5 = hashlib.md5(title.encode('utf-8')).hexdigest()

    if not line:
        return None
    
    s = line.split(" · ")
    if len(s) < 3:
        return None
    if 'Zsuzsanna Zsemlye' in line:
        return None
    line = s[2]
    if not s[2].startswith('Shared with Public'):
        return None
    line = line[18:]

    # find title
    sf = re.sub(r"\d+ commentsLikeCommentShare", "<!!split!!>", line)
    sf = sf.split('<!!split!!>')
    if len(sf) >= 1:
        title = _post_filter(sf[0])
    else:
        title = None

    line = _post_filter(line)

    if not title:
        title = " ".join(line.split(' ')[0:3])

    print(title, '->', line)

    return None
