# 22112202 정보통신공학과 이유준
# HomeWork2_1

print("=====================================")
print(" Decimal    Bit  Octal   Hexadecimal")
print("--------------------------------------")

for i in range(0, 256, 1):
    print("{} {} {} {}".format(i, bin(i), oct(i), hex(i)))
print("======================================")