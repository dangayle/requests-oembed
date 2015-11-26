import re
import requests


endpoints = {
    'youtube': {
        'scheme': 'http*://*.youtube.com/watch*',
        'endpoint': 'http://www.youtube.com/oembed',
        'example': 'https://www.youtube.com/watch?v=F2ZCQfSNMuM'
    },
    'twitter': {
        'scheme': 'http*://twitter.com/*/status/*',
        'endpoint': 'https://api.twitter.com/1/statuses/oembed.json',
        'example': 'https://twitter.com/dangayle/status/284836686171627521'
    },
    'vimeo': {
        'scheme': 'http*://vimeo.com/*',
        'endpoint': 'http://vimeo.com/api/oembed.json',
        'example': 'https://vimeo.com/12676288'
    },
    'gist': {
        'scheme': 'http*://gist.github.com/*',
        'endpoint': '<script src="http://gist.github.com/{}.js"></script>',
        'example': 'https://gist.github.com/2040712'
    },
    'soundcloud': {
        'scheme': 'http*://soundcloud.com/*',
        'endpoint': 'http://soundcloud.com/oembed',
        'example': 'https://soundcloud.com/andrewbird/04-give-it-away'
    }
}


def get_endpoint(url):
    """Get oembed endpoint for a url."""

    for key, values in endpoints.iteritems():

        re_values = str(
            values['scheme']).replace('.', '\.').replace('*', '.*?')
        values['scheme'] = re.compile(re_values)

        if values['scheme'].match(url):
            return values['endpoint']


def get_oembed(url, endpoint, width=480, format="json"):
    """Make oembed request to provider."""

    params = {
        'url': url,
        'width': width,
        'format': format
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None


def gist(url, endpoint):
    return {'html': endpoint.format(url)}


def route(url):
    """Route url to proper embed method."""

    route = None
    e = get_endpoint(url)
    if e == endpoints['gist']['endpoint']:
        route = gist(url, e)
    else:
        route = get_oembed(url, e)
    return route


def oembed(url):
    """Return html from embed request."""

    response = route(url)
    return response['html'].encode('utf-8') if response else url



