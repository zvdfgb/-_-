import csv

with open("data.csv", encoding="utf-8") as f:
    total = sum(int(r["value"]) for r in csv.DictReader(f))
with open("stats.txt", "w", encoding="utf-8") as f:
    f.write(str(total))
