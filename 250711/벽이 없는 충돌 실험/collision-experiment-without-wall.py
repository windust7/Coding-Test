# 0) I/O용 모듈과 가비지 컬렉터
import sys, gc

# 1) 방향 정보 (기존 그대로)
DIR = {"U": 0, "D": 1, "R": 2, "L": 3}
DIR_STR = {0: "^", 1: "v", 2: ">", 3: "<"}
DX, DY = [0, 0, 1, -1], [1, -1, 0, 0]

# ------------------------------------------------------------
# 2) 1개의 테스트케이스만 처리하는 함수로 감싸기
#    => 함수가 끝나면 지역 변수는 전부 스코프 밖으로 사라져 메모리 해제
def solve_one():
    total_ball = int(sys.stdin.readline())
    balls = []                      # [x, y, w, dir, idx]
    INF = 10**9
    min_x, max_x, min_y, max_y = INF, -INF, INF, -INF

    for idx in range(total_ball):
        x, y, w, d = sys.stdin.readline().split()
        x, y, w, d = int(x), int(y), int(w), DIR[d]
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)
        balls.append([x, y, w, d, idx])

    # 3) 0.5칸 방지용 좌표 2배 확장 (기존 그대로)
    for b in balls:
        b[0] = min_x + (b[0] - min_x) * 2
        b[1] = min_y + (b[1] - min_y) * 2
    max_x = min_x + (max_x - min_x) * 2
    max_y = min_y + (max_y - min_y) * 2

    result, time = -1, 0

    # 4) 시뮬레이션 : 2D 리스트 대신 딕셔너리
    while balls:
        time += 1
        hit = False
        new_pos = {}                # (nx, ny) ➟ [nx, ny, w, dir, idx]
        next_balls = []

        for x, y, w, d, idx in balls:
            nx, ny = x + DX[d], y + DY[d]
            if not (min_x <= nx <= max_x and min_y <= ny <= max_y):
                continue            # 경계 밖 → 소멸

            key = (nx, ny)
            if key not in new_pos:  # ⑤ 충돌 X
                new_pos[key] = [nx, ny, w, d, idx]
                next_balls.append(new_pos[key])
            else:                   # ⑥ 충돌 O
                hit = True
                ox, oy, ow, od, oidx = new_pos[key]
                # 무게·인덱스 우선순위 비교
                if w > ow or (w == ow and idx > oidx):
                    # 기존 공을 밀어내고 현재 공이 자리 차지
                    new_pos[key] = [nx, ny, w, d, idx]
                    # next_balls 리스트에서도 교체
                    for k, entry in enumerate(next_balls):
                        if entry[-1] == oidx:
                            next_balls[k] = new_pos[key]
                            break

        if hit:
            result = time
        balls = next_balls          # 다음 턴 준비

    print(result)
    # 7) (선택) 즉시 메모리 반환 요청
    gc.collect()

# ------------------------------------------------------------
# 8) 다중 테스트 케이스 루프
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        solve_one()

if __name__ == "__main__":
    main()