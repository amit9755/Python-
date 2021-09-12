num = 121
pos = 31
for i in range(32):
    if i % 8 == 0:
        print(" ", end="")
    print(num >> (pos-i) & 1, end="")
