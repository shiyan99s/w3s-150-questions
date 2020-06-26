"""
n1 = 3
n2 = 3
n3 = 3
sum = n1 + n2 + n3
if n1==n2==n3:
  print(3*sum)
else:
  print(sum)
"""


def sum(x,y,z):

    sum = x+y+z
    
    if x==y==z:
        print(3*sum)
    else:
        print(sum)

sum(1,2,3)
sum(3,3,3)