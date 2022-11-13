# 22112202 정보통신공학과 이유준
# HomeWork2_3

x = int(input("hexaedcimal x = "), 16) # x를 16진수로 나타냄
y = int(input("hexadecimal y = "), 16) # y를 16진수로 나타냄
z = int(input("hexadecimal z = "), 16) # z를 16진수로 나타냄

hex_x = hex(x) # 16진수로 나타낸 것을 10진수로 바꿈
bin_x = bin(x) # 16진수로 나타낸 것을 2진수로 바꿈
print("x = {}in decimal, {} in bits".format(hex_x, bin_x))

hex_y = hex(y) # 16진수로 나타낸 것을 10진수로 바꿈
bin_y = bin(y) # 16진수로 나타낸 것을 2진수로 바꿈
print("y = {}in decimal, {} in bits".format(hex_y, bin_y))

hex_z = hex(z) # 16진수로 나타낸 것을 10진수로 바꿈
bin_z = bin(z) # 16진수로 나타낸 것을 2진수로 바꿈
print("z = {}in decimal, {} in bits".format(hex_z, bin_z))

print("x & y = {} = {}".format(hex(x & y), bin(x & y))) # x & y
print("x | y = {} = {}".format(hex(x|y),bin(x|y))) # x | y
print("x ^ y = {} = {}".format(hex(x ^ y),bin(x ^ y))) # x ^ y
print("~x = in hex {}, in bin {}".format(hex(~x), bin(~x))) # ~x
print("x << 2 = in hex {}, in bin {}".format(hex(x << 2), bin(x << 2))) # x << 2
print("y >> 2 = in hex {}, in bin {}".format(hex(y >> 2), bin(y >> 2))) # y >> 2
print("z >> 2 = in hex {}, in bin {}".format(hex(z >> 2), bin(z >> 2))) # z >> 2


