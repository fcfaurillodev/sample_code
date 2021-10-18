import pytest
from os import path
from dotenv import load_dotenv

env_file = path.join(path.dirname(path.dirname(path.realpath(__file__))), '.env')
load_dotenv(env_file)
pytest.main(['tests'])