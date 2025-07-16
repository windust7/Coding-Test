n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def merge(low, mid, high):
    result = [None for _ in range(high-low+1)]
    first_low = low
    first_high = mid
    second_low = mid+1
    second_high = high
    first_target = first_low
    second_target = second_low
    result_idx = 0
    for _ in range(len(result)):
        if first_target > first_high:
            result[result_idx] = arr[second_target]
            result_idx += 1
            second_target += 1
        elif second_target > second_high:
            result[result_idx] = arr[first_target]
            result_idx += 1
            first_target += 1
        elif arr[first_target] <= arr[second_target]:
            result[result_idx] = arr[first_target]
            result_idx += 1
            first_target += 1
        else:
            result[result_idx] = arr[second_target]
            result_idx += 1
            second_target += 1
    for idx in range(len(result)):
        arr[low+idx] = result[idx]

def merge_sort(start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        merge(start, mid, end)

merge_sort(0, len(arr)-1)

print(" ".join(map(str, arr)))
