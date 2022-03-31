import json
from .translate import init as googleinit, translate_text
from .verstranslate import translate_buzzwords
from .reddit import init as redditinit, create_post as redditpost
from .fbpreprocess import preprocess

def init_app():
    with open('libs/secret.json') as fh:
        keys = json.load(fh)

    googleinit(keys['google'])
    redditinit(keys['reddit'])

def create_post(line):
    rs = preprocess(line)
    return
    if not rs:
        return None

    title, txt = rs

    txt_trans = translate_text(translate_buzzwords(txt))
    title_trans = translate_text(translate_buzzwords(title))

    resp = redditpost(txt_trans, title_trans)

    return resp
