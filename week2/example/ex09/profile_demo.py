def slow_string_concat():
    res = ""
    for i in range(12000):
        res += str(i)
    return len(res)

def main_pipeline():
    for _ in range(5):
        slow_string_concat()

if __name__ == "__main__":
    main_pipeline()
