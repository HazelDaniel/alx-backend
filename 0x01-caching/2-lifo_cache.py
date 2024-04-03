#!/usr/bin/env python3
"""this module tries to implement a last-in-first-out caching"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """a sub-class of the BaseCaching class that
        implements cache methods. implements a LIFO
           cache using an OrderedDict. performs cache
               eviction by removing the most-recently added entry"""
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """retrieving a cached value in a LIFO based cache"""
        return self.cache_data.get(key, None)
