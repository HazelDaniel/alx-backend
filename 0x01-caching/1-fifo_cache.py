#!/usr/bin/env python3

"""this module tries to implement a first-in-first-out caching"""


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """a sub-class of the BaseCaching class that
        implements cache methods. implements a FIFO
           cache using an OrderedDict"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """updating/creating a cache entry in a FIFO based cache"""

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")
        self.cache_data[key] = item

    def get(self, key):
        """retrieving a cached value in a FIFO based cache"""
        return self.cache_data.get(key, None)
