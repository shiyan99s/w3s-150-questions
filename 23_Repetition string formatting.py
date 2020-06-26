def copies(string, n):
  if len(string) < 2:
    print(n*string)
  else:
    print(n*string[:2])

copies("a", 3)
copies("google", 4)