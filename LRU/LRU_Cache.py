from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity < 0:
            print("invalid capacity")
            self.capacity = None
            return None
        self.capacity = capacity
        self.lru = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if not self.capacity or self.capacity <= 0:
            print("cache capacity error")
            return None
        if key in self.lru:
            return_value = self.lru.pop(key)
        else:
            return -1
        self.lru[key] = return_value
        print("return_value : ", return_value)
        return return_value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        # print("in Set Key : ", key)
        # print("in Set Value : ", value)
        if not self.capacity or self.capacity <= 0:
            print("cache capacity error")
            return None
        if key in self.lru:
            self.lru.pop(key)
        if len(self.lru) == self.capacity:
            self.lru.popitem(last=False)
        self.lru[key] = value


#testcase 1:
# our_cache = LRU_Cache(5)
#
# our_cache.set(1, 1);
# our_cache.set(2, 2);
# our_cache.set(3, 3);
# our_cache.set(4, 4);
#
#
# assert our_cache.get(1) == 1       # returns 1
# assert our_cache.get(2) == 2       # returns 2
# assert our_cache.get(9) == -1      # returns -1 because 9 is not present in the cache
#
# our_cache.set(5, 5)
# our_cache.set(6, 8768689978979797)
#
# assert our_cache.get(6) == 8768689978979797
#
# our_cache.set(7, None)
# assert our_cache.get(7) == None

#testcase 2:
#our_cache = LRU_Cache(-1)
#our_cache.set(1, 1);

#expected output:
# invalid capacity
# cache capacity error

#testcase 3:
#our_cache = LRU_Cache(0)
#our_cache.set(1, 1);

#expected output:
# invalid capacity