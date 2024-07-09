n = int(input())
i = 2
maxi = int(n**0.5)+1
if n != 1 :
    while n > 1 or i <= maxi :
        if(n%i == 0) :
            n /= i
            print(i)
        else  :
            i += 1