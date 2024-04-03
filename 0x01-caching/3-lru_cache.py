#!/usr/bin/env python3
"""this module tries to implement a least-recently-used caching policy"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """a sub-class of the BaseCaching class that
        implements cache methods. implements a LRU
           cache using an OrderedDict. performs cache
               eviction by removing the least recently accessed entry"""

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
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """retrieving a cached value in a LRU based cache"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
