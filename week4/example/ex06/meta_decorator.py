import time
from functools import wraps

def monitor_perf(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = func(*args, **kwargs)
        elapsed = (time.perf_counter() - t0) * 1000
        print(f"[METRIC] 函数 {func.__name__} 调用完成，耗时: {elapsed:.4f} ms")
        return res
    return wrapper

@monitor_perf
def matrix_multiply(n: int):
    return sum(i * i for i in range(n))

matrix_multiply(500000)
