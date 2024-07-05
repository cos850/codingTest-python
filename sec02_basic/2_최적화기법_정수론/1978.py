input()
numbers = set(map(int, input().split()))

def isPn(n) :
    if n < 2 : 
        return False
    for i in range(2, int(n**0.5)+1) :
        if n % i == 0 :
            return False
    return True

r = 0
for n in numbers :
    if isPn(n) : 
        r += 1

print(r)
