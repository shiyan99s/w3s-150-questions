def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):      # Damnnn logic
           lcm = z
           break
       z += 1

   print("LCM of {} and {} is {}".format(x,y,z))

   
(lcm(4, 6))
(lcm(15, 17))