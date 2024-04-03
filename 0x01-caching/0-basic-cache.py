#!/usr/bin/env python3
"""this module implements a basic cache using a hashmap"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a sub-class of the BaseCaching class that
        implements cache methods"""

    def put(self, key, item):
        """updating/creating a cache entry"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """retrieving a cached value"""
        return self.cache_data.get(key, None)
