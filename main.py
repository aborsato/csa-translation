import os
import json
import uuid

import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Add your key and endpoint
key = os.getenv('TRANSLATOR_KEY')
endpoint = os.getenv('TRANSLATOR_ENDPOINT')

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource.
# It can be found in the Azure portal on the Keys and Endpoint page.
location = os.getenv('TRANSLATOR_LOCATION')

PATH = '/translate'
constructed_url = endpoint + PATH

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['fr', 'es', 'pt']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'I would really like to drive your car around the block a few times!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body, timeout=60)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
