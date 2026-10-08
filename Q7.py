import math as m
def gcd_list(list1):
  b=list1[0]
  for a in list1:
    b=m.gcd(a,b)
  return b
