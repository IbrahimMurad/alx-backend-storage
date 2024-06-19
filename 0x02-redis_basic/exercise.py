#!/usr/bin/env python3
""" This module defines a class that uses redis to cache data """
import redis
from uuid import uuid4
from typing import Callable
from typing import Union, Optional
from functools import wraps


def count_calls(f: Callable) -> Callable:
    """ counts the number of times a method is called """
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        if not self._redis.get(f.__qualname__):
            self._redis.set(f.__qualname__, 0)
        self._redis.incr(f.__qualname__)
        return f(self, *args, **kwargs)
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
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes data and stores it in redis with a random generated key """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
        """ gets the data from redis and uses fn to decode it """
        value = self._redis.get(key)
        if value:
            return fn(value) if fn else value
        return None
    
    def get_str(self, key: str) -> str:
        """ gets the data from redis and returns it as a string """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """ gets the data from redis and returns it as an int """
        return self.get(key, fn=int)
