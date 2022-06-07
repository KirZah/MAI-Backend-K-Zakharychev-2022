from cache import LRUCache


cache = LRUCache(3)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('test_key', 'test_val')
cache.set('Jesse', 'James')
print(f"'{cache.get('Jesse')}'")  # вернёт 'James'
cache.remove('Walter')
print(f"'{cache.get('Walter')}'")  # вернёт ''
