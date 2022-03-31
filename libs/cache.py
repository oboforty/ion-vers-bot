import hashlib

_cache: set

def init_cache():
    global _cache

    with open('libs/cache.txt') as fh:
        _cache = set(map(lambda x: x.rstrip('\n'), fh.readlines()))

def has_this_shit_been_posted(post_title):
    global _cache

    _md5 = hashlib.md5(post_title.encode('utf-8')).hexdigest()

    print(_md5, post_title)
    notok = _md5 in _cache
    _cache.add(_md5)

    return notok

def update_cache():
    global _cache

    with open('libs/cache.txt', 'w') as fh:
        fh.write('\n'.join(_cache))
