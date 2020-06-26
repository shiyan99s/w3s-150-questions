def vowel(string):
  count = 0
  for i in string:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
      count += 1
  print("Vowels in {} are {}".format(string, count))

vowel("shiyan")
vowel("aeiou")