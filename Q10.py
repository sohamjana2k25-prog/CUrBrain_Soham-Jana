def count_primes(n):
    if n <= 2:
        return 0
    p_lst = [True] * n
    p_lst[0] = p_lst[1] = False
    i = 2
    while i * i < n:
        if p_lst[i]:
            for j in range(i * i, n, i):
                p_lst[j] = False
        i += 1
    return sum(p_lst)

x = int(input())
print(count_primes(x))
