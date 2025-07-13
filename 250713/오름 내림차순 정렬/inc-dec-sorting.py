n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for item in nums:
    print(item, end=" ")
print()
nums = nums[::-1]
for item in nums:
    print(item, end=" ")