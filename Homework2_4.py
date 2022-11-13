# 22112202 정보통신공학과 이유준
# HomeWork2_4

complex_str_1 = complex(input("input c1(in complex, re + img):")) # 복소수 입력

c1 = complex(complex_str_1)
c2 = complex.conjugate(c1) # 켤레복소수 c2
print("c1 = ", c1)
print("c2 = conjugate of c1 = ", c2)

print("c1 + c2 = ", c1 + c2) # 합
print("c1 - c2 = ", c1 - c2) # 차
print("c1 * c2 = ", c1 * c2) # 곱
print("c1 / c2 = ", c1 / c2) # 나누기
