# [RingCentral Engage Digital Client for Python](https://github.com/ringcentral/engage-digital-client-python)

Simple Python API wrapper for RingCentral Engage Digital api. [api docs](https://engage-api-docs.readthedocs.io/).

[![Build Status](https://travis-ci.org/ringcentral/engage-digital-client-python.svg?branch=release)](https://travis-ci.org/zxdong262/ringcentral-engage-client-python)

## Usage

```python
from ringcentral_engage_digital import RestClient

rc = RestClient(
  RINGCENTRAL_ENGAGE_API_TOKEN,
  RINGCENTRAL_ENGAGE_SERVER_URL
)
r = rc.get('/1.0/roles')
assertEqual(len(r.json['records']) > 0, True)
```

## Test

```bash
cp .sample.env .env
# edit .env fill your server and spi key
npm run test
```

## Credits

Based on [Tyler](https://github.com/tylerlong)'s [https://github.com/tylerlong/ringcentral-python](https://github.com/tylerlong/ringcentral-python).

## License

MIT
