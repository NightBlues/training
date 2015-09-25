__author__ = 'nightblues'

def division_hash(m):
    """m - size of finite field"""
    def hash_func(key):
        return key%m
    return hash_func