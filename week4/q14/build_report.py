with open("report.md", encoding="utf-8") as f:
    text = f.read().strip()
with open("stats.txt", encoding="utf-8") as f:
    total = f.read().strip()
with open("report.txt", "w", encoding="utf-8") as f:
    f.write(f"{text}\nTotal: {total}\n")
