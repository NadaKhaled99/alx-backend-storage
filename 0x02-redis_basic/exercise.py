#!/usr/bin/env python3
""" Writing strings to Redis
"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """ Track call count
    """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """ Wraps called method
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Track args
    """
    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        """ Wraps called method
        """
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


def replay(fn: Callable) -> None:
    """ Check redis
    """
    client = redis.Redis()
    calls = client.get(fn.__qualname__).decode('utf-8')
    inputs = [input.decode('utf-8') for input in
              client.lrange(f'{fn.__qualname__}:inputs', 0, -1)]
    outputs = [output.decode('utf-8') for output in
               client.lrange(f'{fn.__qualname__}:outputs', 0, -1)]
    print(f'{fn.__qualname__} was called {calls} times:')
    for input, output in zip(inputs, outputs):
        print(f'{fn.__qualname__}(*{input}) -> {output}')


class Cache:
    """ Cache class
    """
    def __init__(self) -> None:
        """ Initialize cache object
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes,  int,  float]) -> str:
        """ Stores data in redis
        """
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Get key's value from redis
        """
        client = self._redis
        value = client.get(key)
        if not value:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        """ Convert byte to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts byte to integer
        """
        return int(data)
