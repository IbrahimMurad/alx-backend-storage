#!/usr/bin/env python3
""" In this module we define a function that
stores how many requests a url is made
and cache the result with an expiration time of 10 seconds. """
from requests import get
import redis
from functools import wraps
from typing import Callable



def cache_requests(f: Callable) -> Callable:
    """ Caches the how many requests are made to a certain url
    with an expiration time of 10 seconds. """
    @wraps(f)
    def wrapper(url):
        red = redis.Redis()
        key = "count:{}".format(url)
        if not red.exists(key):
            red.set(key, 0)
        red.incr(key)
        red.expire(key, 10)
        return f(url)
    return wrapper

@cache_requests
def get_page(url: str) -> str:
    """ uses the requests module to obtain
    the HTML content of a particular URL and returns it. """
    r = get(url)
    return r.text
