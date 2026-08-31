import pstats
p = pstats.Stats("profile.stats")
print("--- 按自身耗时 (tottime) 排序 Top 5 ---")
p.strip_dirs().sort_stats("tottime").print_stats(5)
