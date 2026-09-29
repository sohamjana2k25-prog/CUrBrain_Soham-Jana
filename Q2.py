def revdigit(n):
 rev=0
 rem=0
 mul=1
 if n==0:
   return 0
 else:
  if n<0:
    mul=-1
  n=abs(n)
  
  while n!=0:
   rem=n%10
   rev=rev*10+rem
   n=n//10

 return rev*2*mul

n=int (input("enter number"))
ans=revdigit(n)
print (ans)
