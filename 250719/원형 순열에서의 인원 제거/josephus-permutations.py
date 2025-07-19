n, k = map(int, input().split())

# 1부터 n까지 사람들 리스트 생성
people = [i + 1 for i in range(n)]

# 결과를 저장할 리스트
result = []

# 제거할 사람의 인덱스 초기값
index = 0

# 모든 사람이 제거될 때까지 반복
while people:
    index = (index + k - 1) % len(people)
    result.append(people.pop(index))

# 결과 출력
print(' '.join(map(str, result)))