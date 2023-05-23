from flask_caching import Cache
from flask_session import Session

def init_cache(app):
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["CACHE_TYPE"] = "filesystem"
    app.config["CACHE_DIR"] = "/tmp/my_cache"
    app.config["CACHE_DEFAULT_TIMEOUT"] = 60 * 60 * 12  # Set the timeout to 12 hours
    app.config["CACHE_THRESHOLD"] = 500  # Maximum number of cached elements that can be stored on server

    Session(app)
    cache = Cache(app)

    return cache, app