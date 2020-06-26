def repeat(string,n):
  result = ""
  for i in range(n+1):
    result += string
  print(result)

word = "shiyan"
repetition = 2
repeat(word, repetition)