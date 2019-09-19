import pydash as _
try:  # py3
    import urllib.parse as urlparse
except:  # py2
    import urlparse
from requests import Request, Session

version = 'dev'
try:
  with open("version", "r") as fh:
    version = fh.read()
except:
    pass

class RestClient(object):
    def __init__(self, apiToken, server):
        self.server = server
        self.apiToken = apiToken
        self.server = server

    def _bearerAuthorizationHeader(self):
      return f'Bearer {self.apiToken}'

    def request(self, method, url, headers, **kargs):
        urlFinal = urlparse.urljoin(self.server, url)
        userAgentHeader = f'ringcentral-engage-client-python/v${version}'
        if headers is None:
          headers = {}
        headers = _.assign(headers, {
            'Authorization': self._bearerAuthorizationHeader(),
            'User-Agent': userAgentHeader,
            'RC-User-Agent': userAgentHeader,
            'X-User-Agent': userAgentHeader,
        })
        req = Request(
          method,
          urlFinal,
          headers = headers,
          **kargs
        )
        prepared = req.prepare()
        s = Session()
        r = s.send(prepared)
        try:
            r.raise_for_status()
        except:
            raise Exception(
              '{}\n{}\n\nStatus: {}\n Response Text: {}'.format(
                  req.method + ' ' + req.url,
                  'Headers:\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
                  r.status_code,
                  r.text
              )
            )
        return r

    def get(self, url, headers=None, **kargs):
        return self.request('GET', url, headers, **kargs)

    def post(self, url, headers=None, **kargs):
        return self.request('POST', url, headers, **kargs)

    def put(self, url, headers=None, **kargs):
        return self.request('PUT', url, headers, **kargs)

    def patch(self, url, headers=None, **kargs):
        return self.request('PATCH', url, headers, **kargs)

    def delete(self, url, headers=None, **kargs):
        return self.request('DELETE', url, headers, **kargs)
