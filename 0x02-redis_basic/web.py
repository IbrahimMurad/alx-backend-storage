#!/usr/bin/env python3
""" In this module we define a function that
stores how many requests a url is made
and cache the result with an expiration time of 10 seconds. """
from requests import get
import redis


def get_page(url: str) -> str:
    """ uses the requests module to obtain
    the HTML content of a particular URL and returns it. """
    red = redis.Redis()
    count_key = "count:{}".format(url)
    result_key = "result:{}".format(url)
    red.incr(count_key)
    if red.exists(result_key):
        return red.get(result_key).decode('utf-8')
    result = get(url).text
    red.set(result_key, result)
    red.expire(result_key, 10)
    return result
