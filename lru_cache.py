class lru_cache:
    def __init__(self):
        self.cache =[]

    def put(self,item):
        if len(self.cache)==5:
            if item in self.cache:
                  self.cache.remove(item)
                  self.cache.append(item)
           
            else:
                self.cache.pop(0)
                self.cache.append(item)
        else :
            if item in self.cache:
                self.cache.remove(item)
                self.cache.appned(item)
            else:
                self.cache.append(item)

    def get(self,item):
        return item in self.cache
    def get_cache(self):
        return self.cache

def main():
    l=lru_cache()
    l.put(1)
    l.put(2)
    l.put(3)
    print(l.get_cache)