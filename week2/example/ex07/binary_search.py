def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid        # 缺陷点：导致区间无法收缩死循环
        else:
            right = mid - 1
    return left if (left < len(nums) and nums[left] == target) else -1

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9]
    print("Result index:", search(data, 5))
