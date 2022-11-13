#22112202 정보통신공학과 이유준

width, length = map(int, input("input width and length: ").split()) # 가로 세로 길이 값 넣기

area = width * length # area는 가로 곱하기 세로
perimeter = (2 * width) + (2 * length) # perimeter는 (가로 x 2) + (세로 * 2)

print("Rectangle of width ({}) and length ({}) : area ({}), perimeter ({})".format(width, length, area, perimeter)) # print
