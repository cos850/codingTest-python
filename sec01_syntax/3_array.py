#### 배열

# 1. 배열 예시
intList = [0, 0, 0, 0]
strList = ["he", "hi", "ho"]
print(intList, strList)

# 2. 배열로 입력받기
inputIntList = list(map(int, input().split()))
print(inputIntList)

# 3. 문자열로 입력받기
inputStrList = list(input().split())
print(inputStrList)

# 4. 배열의 값만 출력하고 싶다면 * 를 붙이기!
print(*intList) # 0 0 0 0
print(*strList) # he hi ho