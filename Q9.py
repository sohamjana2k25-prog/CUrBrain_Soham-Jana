def cp(a):
    if a < 2:
        return False
    i = 2
    while i * i <= a:
        if a % i == 0:
            return False
        i += 1
    return True

def np(n):
    c = n + 1
    while True:
        if cp(c):
            return c
        c += 1

n = int(input())
print(np(n))
