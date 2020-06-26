def check(list, num):
  if num in list:
    print(True)
  else:
    print(False)

list = [32,13,2,5,0]
check(list, 32)
check(list, -1)