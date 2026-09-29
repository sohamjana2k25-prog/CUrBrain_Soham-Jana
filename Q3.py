def palindrome(n):
    original = n
    rev = 0
    rem = 0
    mul = 1
    if n < 0:
        mul = -1
    n = abs(n)
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    rev = rev * mul
    if original == rev:
        return original
    else:
        return original + rev


n = int(input("enter number"))
ans = palindrome(n)
print(ans)
