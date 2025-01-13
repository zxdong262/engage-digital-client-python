# [RingCentral Engage Digital Client for Python](https://github.com/ringcentral/engage-digital-python)

Simple Python API wrapper for RingCentral Engage Digital api. 

[![Build Status](https://travis-ci.com/ringcentral/engage-digital-python.svg?branch=test)](https://travis-ci.com/ringcentral/engage-digital-python)
[![Coverage Status](https://coveralls.io/repos/github/ringcentral/engage-digital-python/badge.svg?branch=test)](https://coveralls.io/github/ringcentral/engage-digital-python?branch=test)

## Installation

### PIP

```sh
pip3 install ringcentral_engage_voice
# or
pip install ringcentral_engage_voice
```

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

With virtaul env, make sure you have pip3 and python3.6+

```bash
bin/init
source venv/bin/activate
cp .sample.env .env
# edit .env fill all fields
bin/test
```

Without virtaul env, make sure you have pip3 and python3.6+

```sh

pip3 install -r requirements-dev.txt
pip3 install -r requirements.txt
cp .sample.env .env
# edit .env fill all fields
bin/test
```

## Credits

Based on [Tyler](https://github.com/tylerlong)'s [https://github.com/tylerlong/ringcentral-python](https://github.com/tylerlong/ringcentral-python).

## License

MIT
