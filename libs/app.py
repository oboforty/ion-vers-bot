import json
from .translate import init as googleinit, translate_text
from .verstranslate import translate_buzzwords
from .reddit import init as redditinit, create_post as redditpost
from .fbpreprocess import preprocess
from .cache import init_cache, has_this_shit_been_posted, update_cache

def init_app():
    with open('libs/secret.json') as fh:
        keys = json.load(fh)

    init_cache()
    googleinit(keys['google'])
    redditinit(keys['reddit'])

def create_post(line):
    rs = preprocess(line)
    
    if not rs:
        return None

    title, txt = rs

    if has_this_shit_been_posted(title):
        print("-- Already been posted: ", title)
        return None

    return
    txt_trans = translate_text(translate_buzzwords(txt))
    title_trans = translate_text(translate_buzzwords(title))

    resp = redditpost(txt_trans, title_trans)

    print("Posted:", title)

    return True

def close_app():
    update_cache()
