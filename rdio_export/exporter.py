import requests
from requests_oauthlib import OAuth1

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
        self.auth = OAuth1(key, secret)

    def _call(self, group, method, **kwargs):
        data = {'method': method}
        
        # Apply the provided keyword arguments to our data payload
        data.update(kwargs)

        # Make the request
        resp = requests.post('http://api.rdio.com/1/%s' % group,
                auth=self.auth, data=data).json()

        # Check for an error
        if resp.get('status') != 'ok':
            raise RuntimeError(resp.get('message'))

        return resp.get('result')

    def get_user(self, email=None, username=None, extras=RDIO_U_EXTRAS):
        """
        Returns the given user as a dict or None
        """
        if email:
            return self._call('social', 'findUser', email=email, extras=extras)
        if username:
            return self._call('social', 'findUser', vanityName=username, extras=extras)

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
            collection = self._call('collection', 'getAlbumsInCollection',
                    user=user.get('key'), sort=sort, start=start, count=count, extras=extras)

            # Update the size of the last response
            resp_size = len(collection)

            # Update the start index for the next request
            start += resp_size

            # Yield the track results
            for t in collection:
                yield t
