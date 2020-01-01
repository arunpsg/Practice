class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.accessCount = 0
        self.lru = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            self.accessCount += 1
            self.lru[key] = self.accessCount
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        # print("in Set Key : ", key)
        # print("in Set Value : ", value)
        if len(self.cache) >= self.capacity:
            oldItem = self.getOldItem()
            print("oldItem", oldItem)
            self.cache.pop(oldItem)
            self.lru.pop(oldItem)
        self.lru[key] = self.accessCount
        # print("self.lru : ",self.lru)
        self.cache[key] = value

    def getOldItem(self):
        lessAccessCount = 0
        oldItemKey = None
        print("self.lru in getOldItem : ", self.lru)
        for key,value in self.lru.items():
            print("key", key)
            print("value", value)
            if (lessAccessCount == 0) or (value < lessAccessCount) :
                lessAccessCount = value
                oldItemKey = key
        return oldItemKey

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


assert our_cache.get(1) == 1       # returns 1
assert our_cache.get(2) == 2       # returns 2
assert our_cache.get(9) == -1      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

assert our_cache.get(6) == 6      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
