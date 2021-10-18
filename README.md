# Sample App
## Getting started
Pull the source code from the repository.

Repository:`https://github.com/fcfaurillodev/sample_code.git`

Create `.env` for configuration settings.

## Installation

Guide on installing python virtual environment and starting up rewards fetcher app

1 - Installing python virtual environment
```shell
pip install virtualenv
```
This will install python virtualenv package

2 - Creating virtual environment. This tool requires python3.7.4
```shell
virtualenv <path>/venv
```
This will create a virtual environment directory.

3 - Activate virtual environment
```shell
source <path to vitrualenv>/bin/activate
```

4 - Install requirements

Go to project directory and run command below
```shell
pip install -r requirements.txt
```
This will install required python packages.

5 - Setup local Mysql DB and Redis DB

8 - Starting the flask app
```shell
flask run
```

## Running Tests

Run tests

```shell
python -m pytest tests/ -rA
```

Generate Coverage Report
```shell
python -m pytest tests -v --cov-report term --cov-report html:htmlcov --cov-report xml --cov-fail-under=50 --cov=app
```

## Configurations

### Sample .env file for development:
```shell
FLASK_APP=application.py
FLASK_ENV=development
DEBUG=True
BASE_URL=http://127.0.0.1:5000

MYSQL_DB_NAME=sample_app_db
MYSQL_DB_HOST=localhost
MYSQL_DB_PORT=3306
MYSQL_DB_USERNAME=sample_user
MYSQL_DB_PASSWORD=sample_password
MYSQL_DB_CHARSET=utf8mb4

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_CACHE_DB=1
REDIS_PASSWORD=sample_password
REDIS_DECODE_RESPONSE=True
REDIS_SESSION_DB=0
REDIS_SESSION_TTL=60

LOG_LEVEL=DEBUG
```


## API DOCS
- [Merchant API](docs/sample_app.md)


### Sample client insert query for API authentication with client-id: test-client:
```sql
INSERT INTO clients (client_id, name, audience, pub_key, active, created_at, updated_at) VALUES ("test-client", "TEST CLIENT", "f9b3cb87-a0e9-4e1b-8077-f1c6337fd903",  "-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwIcdaE2EKzQCuhMx7x3V
K5RW4i0JFx+gZBo/pJF7y7WQyfPflOQO1WV1JZA1PeOuKj0N9x/TOKf76VLUP3O0
zLxx1PVVbBsdbH720XKldciCegB2vByXKbWN9tp1cI/LtnrFQ53m6tsX4BzWOGAD
VM8QLJAOHSjhdBKXwFbOkKw+QB8w+0ZvY+BRrlrTw6gvPyG/OxH1j/25xDotomH1
Wit1ZSqnbEc8z9bXGMQuAeob21ifqm7ZeRqnSZe6s2chpyYGoko6MPBPKi5Fu+u6
CMzUwmICzkphTjiHnHZzUrT2EiNXpNdGYptsWmVwu6O7ZD0bUzhGNcdzkJ9tp7A5
pQIDAQAB
-----END PUBLIC KEY-----",  1, "1634438916.3618681", "1634438916.3618681");
```

### To create api token for testing:
```shell
python generate_token.py
```
