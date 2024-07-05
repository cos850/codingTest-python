input()

def isPn(n) :
    n = int(n)
    if n < 2 : return 0
    return 1 if all(n % i for i in range(2, int(n**0.5)+1)) else 0

print(sum(map(isPn, input().split())))