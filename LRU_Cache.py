class Key:
    def __init__(self, key, value, lastUsed):
        self.key = key
        self.value = value
        self.lastUsed = lastUsed

class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.opCount = 0

    def insertKeyValuePair(self, key, value):
        self.cache[key] = Key(key, value, self.opCount)

        if len(self.cache) > self.maxSize:
            del self.cache[min(self.cache.items(), key=self.getlastUsed)[0]]
        self.opCount += 1

    def getValueFromKey(self, key):
        if self.cache.get(key) == None:
            return None
        self.cache.get(key).lastUsed = self.opCount
        self.opCount += 1
        return self.cache[key].value

    def getMostRecentKey(self):
        recentKey = max(self.cache.items(), key=self.getlastUsed)
        recentKey[1].lastUsed = self.opCount
        self.opCount += 1
        return recentKey[0]


    def getlastUsed(self, key):
        return key[1].lastUsed
