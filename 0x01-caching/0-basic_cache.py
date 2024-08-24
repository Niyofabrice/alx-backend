#!/usr/bin/env python3
"""
Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Class that inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """
        Function that assings items to the dictionary
        """
        if key or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Function that return the value in self.cache_data based on key
        """
        return self.cache_data.get(key)
