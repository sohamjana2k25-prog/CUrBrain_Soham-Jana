def prefix_sum(list1,k):
  rs=0
  k=abs(k)
  for i in range(len(list1)):
    rs=rs+list1[i]
    if rs%k==0:
      return True
  return False
list1 = list(map(int, input().split()))
k=int(input())
print(prefix_sum(list1,k))
    
