# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 한 줄에서 가장 작은 수 찾기
    main_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, main_value)

print(result) # 최종 답안