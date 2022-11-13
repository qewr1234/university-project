# 22112202 정보통신공학과 이유준
# HomeWork2_2

print("input data one line: ") # print
L = [float(x) for x in input().split(" ")] # 리스트 안에 실수 넣기

print("input data({}) = {}".format(len(L), L)) # 리스트의 길이 및 들어가있는 숫자 확인

min = L[0] # min값 정의
max = L[0] # max값 정의
sum = 0 # sum 초기화

for i in range(0, len(L)): # 반복문
    if max < L[i]: # 만약 max값보다 L[i]크다면
        max = L[i] # max값을 L[i]로 변경
    
for i in range(0, len(L)): # 반복문
    if min > L[i]: # 만약 min값보다 L[i]가 작다면
        min = L[i] # min값을 L[i]로 변경

for i in range(0, len(L)): # 반복문
    sum += L[i] # sum값에 L[i]값 전부 더하기

average = sum / len(L) # sum값을 L의 크기로 나눔

print("min = {}, max = {}, average = {}".format(min, max, average)) # print