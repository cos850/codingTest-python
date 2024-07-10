N = int(input())
n = N
result = []
i = 2
while i <= int(N**0.5)+1 :
    if n%i == 0 :
        result.append(i)
        n //= i
    else :
        i += 1

if n != 1 : result.append(n)

print(len(result))
print(*result)