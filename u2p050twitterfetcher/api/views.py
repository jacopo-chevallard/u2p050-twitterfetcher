from flask import make_response, request, jsonify, Response
import json
import snscrape.modules.twitter
import time
import random

from . import api_bp

@api_bp.route("/print_hello", methods=["GET"])
def print_hello():
    person_name = request.args.get('person_name', 'World')
    return make_response(json.dumps({"hello": person_name}), 200)


@api_bp.route("/fetch/twitter", methods=["GET"])
def fetch_twitter():
    content = request.args.get('content', None)
    scraper = snscrape.modules.twitter.TwitterSearchScraper(content)
    tweets = [tweet.json() for tweet in scraper.get_items()]
    return jsonify(tweets)

@api_bp.route("/stream/twitter", methods=["GET"])
def stream_twitter():
    content = request.args.get('content', None)
    delay = 10
    def generate():
        old_tweets = set()
        while True:
            scraper = snscrape.modules.twitter.TwitterSearchScraper(content)
            new_tweets = set(tweet.json() for tweet in scraper.get_items())
            for new_tweet in new_tweets.difference(old_tweets):
                yield f"data: {new_tweet}\n\n"
            old_tweets = new_tweets
            jitter = random.uniform(0.5, 1.5)
            sleep_time = delay * jitter
            time.sleep(sleep_time)
    return Response(generate(), mimetype='text/event-stream')
