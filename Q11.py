def mod_add(list1):
  mod=(10**9)+7
  ns=0
  for i in list1:
    ns=(i+ns)%mod
  return ns
list1 = list(map(int, input().split()))
print(mod_add(list1))
    
