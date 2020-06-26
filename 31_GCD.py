def gcd(x,y):
  gcd = 1
  
  if x % y == 0:
    print(y)
  for i in range(int(y/2), 0, -1):
    if x % i == 0 and y % i == 0:
      gcd = i
      break
  print(gcd)

gcd(12, 17)
gcd(4, 6)