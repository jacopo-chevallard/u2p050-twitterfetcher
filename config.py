import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class BaseConfig:
    LISTEN_HOST = os.getenv("LISTEN_HOST")
    LISTEN_PORT = os.getenv("LISTEN_PORT")

    SECRET_KEY = os.getenv("SECRET", "hard to guess secret key")
    TOKEN_SECRET = os.getenv("TOKEN_SECRET")

    ES_HOST = os.getenv("ES_HOST")
    ES_PORT = os.getenv("ES_PORT")
    ES_SCHEME = os.getenv("ES_SCHEME")

    PROCESSING_API_TOKEN = os.getenv("PROCESSING_API_TOKEN")
    PROCESSING_API_URL = os.getenv("PROCESSING_API_URL")
    PROCESSING_API_VERSION = os.getenv("PROCESSING_API_VERSION")

    PROCESSING_API_RATE_LIMIT = os.getenv("PROCESSING_API_RATE_LIMIT")

# Set Development Config Variables
class DevelopmentConfig(BaseConfig):
    ENV = "development"
    TESTING = True
    DEBUG = True
    TEST_PROJECT_KEY = os.getenv("TEST_PROJECT_KEY")


# Set Development Config Variables
class TestConfig(BaseConfig):
    ENV = "testing"
    TESTING = True
    DEBUG = True
    TEST_PROJECT_KEY = os.getenv("TEST_PROJECT_KEY")

# Set Production Config Variables
class ProductionConfig(BaseConfig):
    ENV = "production"
    TESTING = False
    DEBUG = True