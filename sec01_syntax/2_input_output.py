#### 타입별 입력받기

# 1. 문자열 타입 (default)
string = input()
print(string)

# 2. 숫자 타입 
number = int(input())   # 문자열 타입으로 받아지기 때문에 숫자형으로 변경
print(number)

# 3. 문자열 (문자별로 나눠서 받기)
first, second, third = map(str, input().split())
print(first, second, third)

# 4. 수열
first, second, third = map(int, input().split())
print(first, second, third)