def k_n(n,k):
  list1=[]
  for i in range (1,int(n**(1/2))+1):
      if n%i==0:
       list1.append(i)
       if i!=n//i:
        list1.append(n//i)
  list1.sort()
  if (k> len(list1)):
    return -1
  return list1[k-1]

n=int ( input ())
k=int (input())
print(k_n(n,k))
