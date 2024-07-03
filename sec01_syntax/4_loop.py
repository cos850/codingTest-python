#### 반복문

# 1. for문
print('for문 1) 5번 반복')
for _ in range(5):
    print("hello")

print('for문 2) 변수를 받아서 3번 반복')
for n in range(3):  
    print(n)        # n: 0 ~ 2

print('for문 3) 5~8 사이의 범위 반복')
for n in range(5, 8):  
    print(n)        # n: 5 ~ 7


# 2. while문
print('while문')
n = 0
while n < 5:
    print(n)    # 0 ~ 4
    n += 1