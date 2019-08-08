import json
import requests


def get_show(base_url, api_key):
    response = requests.get(base_url + "shows/query", params={"apikey": api_key, "year": 2019, "month": 7, "day": 14})
    content = json.loads(response._content)
    print(json.dumps(content, indent=4))


def get_setlist(base_url, api_key):
    response = requests.get(base_url + "setlists/get", params={"apikey": api_key, "showid": 1547482678})
    content = json.loads(response._content)
    print(json.dumps(content, indent=4))
