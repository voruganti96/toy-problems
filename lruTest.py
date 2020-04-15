from lru_cache import lru_cache

class lruTest():
    def  __init__(self):
        self.LRU= lru_cache()

    def testPut(self,item):
        self.LRU.put(item)

    def testGet(self, item):
        return self.LRU.get(item)

    def testGet_cache(self):
        return self.LRU.get_cache()

def main():
        lt=lruTest()  
        lt.testPut(1)
        lt.testPut(2)
        lt.testPut(3)
        lt.testPut(4)
        lt.testPut(5)
        assert [1,2,3,4,5] == lt.testGet_cache()
        assert True == lt.testGet(5)
        lt.testPut(1)
        assert [2,3,4,5,1] == lt.testGet_cache()
        print("all test cases passed")

if __name__ == '__main__':
    main()
