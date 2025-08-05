#dictionar pt cache
fibonacci_cache={}

#in cazul in care exista
def get_from_cache(n: int):
    return fibonacci_cache.get(n)

#salveaza rezultatul in cache
def save_to_cache(n: int, result: int):
    fibonacci_cache[n] = result