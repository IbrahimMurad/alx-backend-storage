#!/usr/bin/env python3
""" In this module we define a function that
stores how many requests a url is made
and cache the result with an expiration time of 10 seconds. """
from requests import get
import redis
from typing import Callable


def caching_decorator(method: Callable) -> Callable:
    """ get_page wrapper that caches the result
    with an expiration time of 10 seconds. """
    def wrapper(url: str) -> str:
        """ wrapper function """
        red = redis.Redis()
        count_key = "count:{}".format(url)
        result_key = "result:{}".format(url)
        red.incr(count_key)
        if red.exists(result_key):
            return red.get(result_key).decode('utf-8')
        red.set(count_key, 1)
        result = method(url)
        red.setex(result_key, 10, result)
        return result
    return wrapper


@caching_decorator
def get_page(url: str) -> str:
    """ uses the requests module to obtain
    the HTML content of a particular URL and returns it. """
    r = get(url)
    return r.text
