def memoize(func):
    """Return a wrapper that caches results in an enclosing dict."""
    cache = {}  # Enclosing scope

    def wrapper(n):
        if n in cache:
            print("⏱️ Беремо з кеша")  # для наочності
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


@memoize
def fib(n: int) -> int:
    """Compute n-th Fibonacci number (naive recursion)."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Example usage
print(fib(3))   # перший виклик — обчислює і зберігає в кеш
print(fib(3))   # другий виклик — бере результат з кеша