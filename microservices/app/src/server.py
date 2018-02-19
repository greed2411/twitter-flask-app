from src import app
from flask import render_template, request
# from flask import jsonify

import base64
import requests
import urllib.parse
import json
import datetime
import time

# twitter part

client_key = 'i4TjaBtGXdDskozAcnZfWOKjd'
client_secret = 'jzIzdVZzLPzkoLAkuiM0lAkTwBQ3w74hHQNWpPxHlnjiyjJFtZ'

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')
base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)
auth_headers = {'Authorization': 'Basic {}'.format(b64_encoded_key),
                'Content-Type':
                'application/x-www-form-urlencoded;charset=UTF-8'}
auth_data = {'grant_type': 'client_credentials'}
auth_resp = requests.post(auth_url, headers=auth_headers,
                          data=auth_data)
access_token = auth_resp.json()['access_token']
search_headers = {'Authorization': 'Bearer {}'.format(access_token)}
search_url = '{}1.1/search/tweets.json?'.format(base_url)


@app.route("/")
def home():
    return render_template('index.html')

# Uncomment to add a new URL at /new
@app.route('/query/')
def home_page():
    query = request.args.get('q', '')
    search_params = {'q': query, 'result_type': 'recent', 'count': 100}

    response = requests.get(search_url +
                            urllib.parse.urlencode(search_params),
                            headers=search_headers)
    body = json.loads(response.text)
    result_count = len(body['statuses'])
    now = datetime.datetime.utcnow()
    raw_oldest_tweet_at = body['statuses'][-1]['created_at']
    oldest_tweet_at = datetime.datetime.strptime(
                                                raw_oldest_tweet_at,
                                                '%a %b %d %H:%M:%S +0000 %Y')
    seconds_diff = time.mktime(now.timetuple()) \
        - time.mktime(oldest_tweet_at.timetuple())
    tweets_per_second = float(result_count) / seconds_diff
    return render_template("results.html", query = query, tweets_per_second =tweets_per_second, tweet_data=body, result_count=result_count, raw_oldest_tweet_at=raw_oldest_tweet_at)


# @app.route("/json")
# def json_message():
#     return jsonify(message="Hello World")
