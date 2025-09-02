def memoize(func):
    """Return a wrapper that caches results in an enclosing dict."""
    cache = {}  # Enclosing scope

    def wrapper(n):
        # cache з Enclosing scope
        if n in cache:
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


# --- Demo (no main) ---
print(fib(10))   # первое вычисление
print(fib(12))   # второе — из кеша