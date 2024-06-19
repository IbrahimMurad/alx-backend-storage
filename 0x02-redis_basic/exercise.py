#!/usr/bin/env python3
""" This module defines a class that uses redis to cache data """
import redis
from uuid import uuid4
from typing import Callable
from typing import Union, Optional


class Cache:
    """ takes data and caches it and stores it in redis """
    def __init__(self) -> None:
        """ instantiate the class """
        self._redis = redis.Redis(
            host='localhost',
            port=6379
        )

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes data and stores it in redis with a random generated key """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Optional[Union[str, bytes, int, float]]:
        """ gets the data from redis and uses fn to decode it """
        if fn:
            return fn((self._redis).get(key))
        if self._redis.get(key):
            return (self._redis).get(key)
        return None
    
    def get_str(self, key: str) -> str:
        """ gets the data from redis and returns it as a string """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """ gets the data from redis and returns it as an int """
        return self.get(key, fn=int)
