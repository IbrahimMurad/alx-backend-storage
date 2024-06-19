#!/usr/bin/env python3
""" This module defines a class that uses redis to cache data """
import redis
from uuid import uuid4
from typing import Callable, Union, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ counts the number of times a method is called """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ counts the number of times a method is called """
        if not self._redis.exists(method.__qualname__):
            self._redis.set(method.__qualname__, 0)
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """ a function wrapper to store its history """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ stores the history of inputs and outputs for the passed function """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper

class Cache:
    """ takes data and caches it and stores it in redis """
    def __init__(self) -> None:
        """ instantiate the class """
        self._redis = redis.Redis(
            host='localhost',
            port=6379
        )
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes data and stores it in redis with a random generated key """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
        """ gets the data from redis and uses fn to decode it """
        if self._redis.exists(key):
            return fn(self._redis.get(key)) if fn else self._redis.get(key)
        return None
    
    def get_str(self, key: str) -> str:
        """ gets the data from redis and returns it as a string """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """ gets the data from redis and returns it as an int """
        return self.get(key, fn=int)
