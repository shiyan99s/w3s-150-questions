n = int(input("Input an integer : "))
n1 = int( "%i" %n )
n2 = int( "%i%i" %(n,n) )
n3 = int( "%i%i%i" %(n,n,n) )
print("Expected sum = {}".format(n1+n2+n3))

