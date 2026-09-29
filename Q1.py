def count_digits(n):
 count =0
 if n==0:
   return False
 else:
  n=abs(n)
  while n!=0:
   n=n//10
   count=count+1
 if count%2==0:
   return True 
 else:
   return False

n=int (input("enter number"))
ans=count_digits(n)
print (ans)
