n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
original = nums[:]
nums.sort(reverse=True)
# print(nums, original)

_max = -int(1e9)

for idx in range(n):
    _max = max(_max, original[idx]+nums[idx])

print(_max)