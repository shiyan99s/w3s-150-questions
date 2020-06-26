def count(num_list, num):
  count = 0
  for i in num_list:
    if i == 4:
      count += 1
  print("Repetition of {} in {} is {}".format(num, num_list, count ))

list = [4,4,4,4,4,4]
int = 4
count(list, int)