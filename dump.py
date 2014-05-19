import sys

from rdioapi import Rdio
from settings_local import RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET

def uprint(msg):
    """
    Unbuffered print.
    """
    sys.stdout.write("%s\n" % msg)
    sys.stdout.flush()

r = Rdio(RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET, {})

## findUser

#r.call('findUser', email='tristan.waddington@gmail.com')
userKey = r.call('findUser', vanityName='twaddington').get('key')

## getAlbumsInCollection

per_page = 150

total = 0
page_size = per_page

collection = []
while (per_page == page_size):
    # ...
    results = r.call('getAlbumsInCollection', user=userKey, sort='artist',
            start=total, count=per_page, extras='-*,name,artist,displayDate,shortUrl,albumKey,artistKey')

    # ...
    page_size = len(results)

    # ...
    total += page_size

    # ...
    collection.extend(results)

    # ...
    uprint("Total: %s, page_size: %s" % (total, page_size))

uprint("Found %d albums!" % total)

last_artist = None
for album in collection:
    artist = album.get('artist')

    # ...
    if last_artist != artist:
        uprint("\n%s" % artist)

        # ...
        last_artist = artist

    # ...
    uprint("  %s" % album.get('name'))
