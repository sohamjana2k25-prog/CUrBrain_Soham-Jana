def mod_pow(base,pow,mod):
  res=1%mod
  for i in range(pow):
    res=(res*base)%mod
  return res
base=int(input())
pow=int(input())
mod=int(input())
print(mod_pow(base,pow,mod))
    
