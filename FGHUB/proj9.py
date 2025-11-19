import random
num = random.randint(0, 100)
num += 1

for i in range(num):
    num -= 1
    print(num)
