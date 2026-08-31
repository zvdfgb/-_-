import tracemalloc

def load_with_list(n):
    return [x * 2 for x in range(n)]

def load_with_generator(n):
    return (x * 2 for x in range(n))

def measure(func, n):
    tracemalloc.start()
    res = func(n)
    total = sum(res)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"[{func.__name__:<20}] Sum={total}, Peak Memory={peak / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    N = 1_000_000
    measure(load_with_list, N)
    measure(load_with_generator, N)
