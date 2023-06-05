from flask import make_response, request, jsonify, Response, current_app
import json
import snscrape.modules.twitter
import time
import random
import os
from datetime import datetime
import re

from . import api_bp
from ..utils.format import reformat_output_payload

_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"

@api_bp.route("/print_hello", methods=["GET"])
def print_hello():
    person_name = request.args.get('person_name', 'World')
    return make_response(json.dumps({"hello": person_name}), 200)


@api_bp.route("/fetch/twitter", methods=["GET", "POST"])
def fetch_twitter():
    content = request.args.get('request', None, type=str)
    n_tweets = request.args.get('n_tweets', 100, type=int)

    if current_app.config.get('ENV') in ['testing', 'development']:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(base_dir, 'data', "u2p050.jsonl"), 'r') as json_file:
            tweets = json.load(json_file)
            print(tweets[0])
            tweets = [reformat_output_payload(tweet) for tweet in tweets]
    else:
        scraper = snscrape.modules.twitter.TwitterSearchScraper(content)
        tweets = [] ; _n = 0
        for i, tweet in enumerate(scraper.get_items()):
            try:
                tweets.append(reformat_output_payload(tweet.json()))
                _n += 1
            except:
                pass
            if _n == n_tweets:
                break

    if request.method == 'POST':
        data = request.get_json()
        
        if 'newer' in data:
            date = datetime.strptime(data["newer"], _DATE_FORMAT)
            _tweets = []
            for tweet in tweets:
                _date = datetime.strptime(tweet['date'], _DATE_FORMAT)
                if _date > date:
                    _tweets.append(tweet)
            tweets = _tweets

        if 'keep_fields' in data:
            tweets = [{k: v for k, v in tweet.items() if k in data['keep_fields']} for tweet in tweets]

        if 'regex' in data:
            for tweet in tweets:
                tweet['content'] = re.sub(data['regex'], '', tweet['content']).strip()

    tweets.sort(key=lambda x: datetime.strptime(x['date'], _DATE_FORMAT), reverse=True)

    data_str = json.dumps(tweets, ensure_ascii=False)

    # Encode the string as UTF-8, ignoring errors
    data_bytes = data_str.encode('utf-8', 'ignore')

    # Decode the bytes back into a string, also ignoring errors.
    # This step removes any characters that could not be encoded as UTF-8.
    safe_str = data_bytes.decode('utf-8', 'ignore')
            
    return Response(safe_str, mimetype='application/json')

@api_bp.route("/stream/twitter", methods=["GET"])
def stream_twitter():
    content = request.args.get('request', None)
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
