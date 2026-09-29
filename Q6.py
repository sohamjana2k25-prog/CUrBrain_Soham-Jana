def search(n,a,b):
    rem = 0
    ac = 0
    bc = 0
    if n == 0:
        if a == 0:
            ac = 1
        if b == 0:
            bc = 1
    else:
        while n != 0:
            rem = n % 10
            if rem == a:
                ac = ac + 1
            if rem == b:
                bc = bc + 1
            n = n // 10
    return abs(ac-bc)

n = int(input("enter number"))
a = int(input("enter a"))
b = int(input("enter b"))

ans = search(n,a,b)
print(ans)
