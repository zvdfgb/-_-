import sys

review_comments = [
    "[Nit]: Spacing after comma in argument list.",
    "[Suggestion]: Consider caching regex pattern.",
    "[Blocking]: Missing null check before accessing array index."
]

blocking = [c for c in review_comments if "[Blocking]" in c]
print(f"Total Comments: {len(review_comments)}, Blocking: {len(blocking)}")

if blocking:
    print("[FAIL] Merge blocked by unaddressed Blocking issues:")
    for b in blocking:
        print("  *", b)
    sys.exit(1)
print("[PASS] Merge allowed.")
