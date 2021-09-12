import sys
print("################ BitWisee operator with positive number ###########################")

a = 10  # 10 = 0000 1010
b = 20  # 20 = 0001 0100

Result = a & b
print("Bitwise AND operator {} & {} = {}".format(a, b, Result))  # 0

Result = a | b
print("Bitwise OR operator {} | {} = {}".format(a, b, Result))  # 30

Result = a ^ b
print("Bitwise XOR operator {} ^ {} = {}".format(a, b, Result))  # 30

Result = ~ a
print("Bitwise compliment operator ~{} ={}".format(a, Result))  # -11

pos = 2
Result = a << pos
print("Bitwise << operator {} = {}".format(a, Result))  # 40

pos = 2
Result = a >> pos
print("Bitwise >> operator {} = {}".format(a, Result))  # 2

print("###################Bitwise operator with Negative number #########################")

a = -10  # -10 =
b = -20  # -20 =

Result = a & b
print("Bitwise AND operator {} & {} = {}".format(a, b, Result))  # 0

Result = a | b
print("Bitwise OR operator {} | {} = {}".format(a, b, Result))  # 30

Result = a ^ b
print("Bitwise XOR operator {} ^ {} = {}".format(a, b, Result))  # 30

Result = ~ a
print("Bitwise compliment operator ~{} ={}".format(a, Result))  # -11

pos = 2
Result = a << pos
print("Bitwise << operator {} = {}".format(a, Result))  # 40

pos = 2
Result = a >> pos
print("Bitwise >> operator {} = {}".format(a, Result))  # 2

print("############# Set a bit ##############")

m = 10
m = m | (1 << 5)
print("Set 2 bit of the: ", m)  # 14


print("############# Clear a bit ##############")

m = 10
m = m & ~(1 << 2)
print("Clear 2 bit of the: ", m)  # 10

print("############# Compliment a bit ##############")

m = 10
m = m ^ (1 << 2)
print("Compliment 2 bit of the: ", m)  # 14
