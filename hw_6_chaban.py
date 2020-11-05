def do_cache_decorator(maxsize=None):
    def decorator(func):
        cache = {}

        def cache_func(*args):
            if args in cache:
                return cache[args]
            if maxsize is not None and len(cache) == maxsize:
                cache.popitem()
            result = func(*args)
            cache[args] = result
            print(cache)
            return result
        return cache_func
    return decorator


@do_cache_decorator(maxsize=3)
def get_value(a, b):
    return a ** b


get_value(6, 7)
get_value(6, 4)
get_value(6, 7)
get_value(5, 7)
get_value(6, 3)
