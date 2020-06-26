def colors(list1, list2):
  new_string = ""
  for i in list1:
    if i not in list2:
      new_string += i
  print("{} not present in {}".format(new_string, list2))
      

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])


# Alternate
colors(color_list_1, color_list_2)
print(color_list_1.difference(color_list_2))


# Alternate
for i in color_list_1:
    if i not in color_list_2:
        print(i, end = " ")
