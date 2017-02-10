import random
import collections
import math
import datetime

def filter_shuffle(seq):
    try:
        result = list(seq)
        random.shuffle(result)
        return result
    except:
        return seq

def filter_as_set(seq):
    if not isinstance(seq, collections.Iterable):
        seq = [seq]

    try:
        result = set(seq)
        return result
    except:
        return seq


def filter_insert_products(s, products):

    product_placeholder = '<!-- insert_products_here -->'
    if product_placeholder in s:
        i = s.index(product_placeholder)
        return s[:i] + products + s[i:]

    else:
        split_on_h2 = s.split('<h2')
        # Only insert ads on longer articles (with >1 section)
        if len(split_on_h2) > 1:
            where = int( round( len(split_on_h2) / 2.0 ) )-1 # Insert near the middle, erring earlier
            split_on_h2[where] = split_on_h2[where] + products
        return '<h2'.join(split_on_h2)


def filter_readtime(s):
    chart = len(s) / 1000
    wordt = len(s.split(' ')) / 200

    reading_time_mins = max([chart, wordt])

    return max(1, int(math.ceil(reading_time_mins/5.0)*5) )


def filter_subcattoc(articles):
    """
    Take a list of articles, and identify all the subcategories as a
    hierarchical tree. Group articles under subcats. Article series (>1)
    grouped as a single entry, with (1|2|3) links.
    """
    toc = dict()
    base = min(len(a.subcategories) for a in articles)
    # we show articles on base, <cats+articles> at base + 1, <cats> at base + 2

    article_list = collections.defaultdict(list)
    articat_dict = collections.defaultdict(dict)
    categor_dict = collections.defaultdict(dict)

    for a in articles:
        scs = a.subcategories
        depth = len(scs)
        # Group together articles in the same series
        if 'series' in a.metadata:
            key = a.metadata['series']
        else:
            key = a.title

        # Treat different article levels differently
        if depth == base:
            article_list[key].append(a)

        elif depth == base+1:
            subcat = scs[-1]

            if key not in articat_dict[subcat]:
                articat_dict[subcat][key] = []
            articat_dict[subcat][key].append(a)

        elif depth == base+2:
            parent, subcat = scs[-2], scs[-1]
            if subcat not in categor_dict[parent]:
                categor_dict[parent][subcat] = 0
            else:
                categor_dict[parent][subcat] += 1

    articat_d = collections.defaultdict(list)
    for k, _v in articat_dict.items():
        for _, v in _v.items():
            articat_d[k].append(v)

    # Sort top articles by date
    article_list = article_list.values()
    article_list.sort(key=lambda a: a[0].date, reverse=True)

    # Order categories alphabetically
    articat_d = collections.OrderedDict(sorted(articat_d.items(), key=lambda x: x[0]))

    return article_list, articat_d, categor_dict


def filter_subcats(s):
    subcats = [s]
    while hasattr(s, 'parent'):
        s = s.parent
        subcats.insert(0, s)

    return subcats[0], subcats[1:]


def filter_is_recent(dt):
    tz_info = dt.tzinfo
    now = datetime.datetime.now(tz_info)
    return dt > now - datetime.timedelta(weeks=12)


def filter_incrange(v, minv, maxv):
    v += 1
    if v >= maxv:
        v = minv
    return v
