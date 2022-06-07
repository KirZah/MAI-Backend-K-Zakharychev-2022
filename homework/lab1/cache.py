from typing import Dict


class LRUCache:
    __capacity = None
    __counter = 0
    __cache: Dict[str, str] = dict()
    __last_used_keys: list = []

    def __init__(self, capacity: int=10) -> None:
        self.__capacity = capacity

    def get(self, key: str) -> str:
        print(f"========== GET {key=} ==========")
        print(f"\t{self.__last_used_keys}")
        print(f"\t{self.__cache}")
        if key in self.__cache:
            self._update_key(key)
            return self.__cache[key]
        else:
            return ''

    def set(self, key: str, value: str) -> None:
        print(f"========== set {key=} {value=} ==========")

        print(f"SET - BEFORE")
        print(f"\t{self.__last_used_keys}")
        print(f"\t{self.__cache}")

        if key in self.__cache:
            print(f"\tkey in cache")
            self._update_key(key)
        else:
            print(f"\tkey NOT in cache")
            if self.__counter < self.__capacity:
                print(f"\t\t{self.__counter} < {self.__capacity}")
                self.__last_used_keys.append(key)
                self.__counter += 1
                print(f"\t\tcounter = {self.__counter}")
            else:
                print(f"\t\t{self.__counter} >= {self.__capacity}")
                oldest_key = self.__last_used_keys.pop(0)
                del self.__cache[oldest_key]
                self.__last_used_keys.append(key)

        self.__cache[key] = value

        print(f"SET - AFTER")
        print(f"\t{self.__last_used_keys}")
        print(f"\t{self.__cache}")

    def remove(self, key: str) -> None:
        print(f"========== REMOVE - BEFORE ==========")
        print(f"\t{self.__last_used_keys}")
        print(f"\t{self.__cache}")

        self.__last_used_keys.remove(key)
        del self.__cache[key]

    def _update_key(self, key) -> None:
        print(f"update_key")

        print(f"\t{self.__last_used_keys}")
        print(f"\t{self.__cache}")

        # pop key from the list if it exists
        self.__last_used_keys.remove(key)
        # throw this key to the end of list
        self.__last_used_keys.append(key)



