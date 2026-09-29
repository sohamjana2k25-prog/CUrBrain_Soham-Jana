def diff(n):
    rem = 0
    sum=0
    mul=1
    n = abs(n)
    while n != 0:
        rem = n % 10
        sum=sum+rem 
        mul=mul*rem
        n = n // 10
    return mul-sum


n = int(input("enter number"))
ans = diff(n)
print(ans)
