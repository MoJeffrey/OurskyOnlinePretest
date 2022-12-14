import math
import time


class Cache:
    __MaxDataNum = 5

    __DataValue: dict = None
    __DataWeight: dict = None
    __DataLastAccessedTime: dict = None

    def __init__(self):
        self.__Data = {}
        self.__DataWeight = {}
        self.__DataLastAccessedTime = {}

    def __getScore(self, key) -> int:
        """
        The Score Formula
        weight ∕ [ln(current_time - last_accessed_time + 1) + 1]
        :param key:
        :return:
        """
        return self.__DataWeight[key] / (math.log(time.time() - self.__DataLastAccessedTime[key] + 1) + 1)

    def __remove(self, key) -> None:
        """
        remove data in cache
        :param key:
        :return:
        """
        self.__Data.pop(key)
        self.__DataWeight.pop(key)
        self.__DataLastAccessedTime.pop(key)

    def get(self, key):
        if key in self.__Data:
            self.__DataLastAccessedTime[key] = time.time()
            return self.__Data[key]
        else:
            return -1

    def put(self, key, value, weight: int):
        if len(self.__Data) == self.__MaxDataNum:

            FirstKey = list(self.__Data.keys())[0]
            RemoveKey = FirstKey
            LowestScore = self.__getScore(FirstKey)

            for DataKey in self.__Data:
                NowScore = self.__getScore(DataKey)
                if LowestScore > NowScore:
                    LowestScore = NowScore
                    RemoveKey = DataKey

            self.__remove(RemoveKey)

        self.__Data[key] = value
        self.__DataWeight[key] = weight


if __name__ == '__main__':
    C = Cache()
    C.put('A', 'A', 1)
    print(C.get('A'))
    C.put('B', 'B', 1)
    print(C.get('B'))
    C.put('C', 'C', 1)
    print(C.get('C'))
    C.put('D', 'D', 1)
    print(C.get('D'))
    C.put('E', 'E', 1)
    print(C.get('E'))
    C.put('F', 'F', 1)
    print(C.get('F'))
    print(C.get('A'))

