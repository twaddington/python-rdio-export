from rdioapi import Rdio

RDIO_U_EXTRAS = ','.join((
    'username',
))

RDIO_C_PER_PAGE = 50
RDIO_C_SORT_BY = 'artist'
RDIO_C_EXTRAS = ','.join((
        '-*',
        'name',
        'artist',
        'displayDate',
        'shortUrl',
        'albumKey',
        'artistKey',
))


class RdioExporter():
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

        # Initialize our client
        self.rdio = Rdio(key, secret, {})

    def get_user(self, email=None, username=None, extras=RDIO_U_EXTRAS):
        """
        Returns the given user as a dict or None
        """
        if email:
            return self.rdio.call('findUser', email=email, extras=extras)
        if username:
            return self.rdio.call('findUser', vanityName=username, extras=extras)

    def get_collection(self, user):
        """
        Returns the entire collection for the given user.

        This method buffers the entire collection to memory before returning.
        You should generally prefer to use the more efficient collection method.
        """
        collection = []

        for t in self.collection(user):
            collection.append(t)

        return collection

    def collection(self, user, sort=RDIO_C_SORT_BY, count=RDIO_C_PER_PAGE,
            extras=RDIO_C_EXTRAS):
        """
        Generator method to efficiently iterate over the collection for the
        given user
        """
        start = 0
        resp_size = count

        # Continue fetching in batches until the last response is smaller
        # than the page size (count).
        while (resp_size == count):
            collection = self.rdio.call('getAlbumsInCollection',
                    user=user.get('key'), sort=sort, start=start, count=count, extras=extras)

            # Update the size of the last response
            resp_size = len(collection)

            # Update the start index for the next request
            start += resp_size

            # Yield the track results
            for t in collection:
                yield t
