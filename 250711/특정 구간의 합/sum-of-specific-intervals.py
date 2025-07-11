n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
for idx in range(m):
    result_list = arr[queries[idx][0]-1:queries[idx][1]]
    print(sum(result_list))