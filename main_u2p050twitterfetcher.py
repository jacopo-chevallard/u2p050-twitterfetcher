"""Main is the entry point of your u2p050 TwitterFetcher application."""
from u2p050twitterfetcher.app import init_app

app = init_app()

if __name__ == "__main__":
    app.run(port=app.config.get("LISTEN_PORT"), host=app.config.get("LISTEN_HOST"))
