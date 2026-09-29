def even0(n):
    rem = 0
    list1=[]
    n = abs(n)
    while n != 0:
        rem = n % 10
        if rem%2==0:
          list1.append(0)
        else:
          list1.append(rem)
        n = n // 10
    list1.reverse()
    return list1


n = int(input("enter number"))
ans = even0(n)
print(ans)
