def new_string(line):
  if len(line) >= 2 and line[:2] == "Is":
    print(line)
  else:
    print("Is"+line)
  
new_string("Array")
new_string("Is")
new_string("isis")

# Membership function
def membership(word):
  if word in line:
    print(True)
  else:
    print(False)
    
line = "googlewordgoogle"
membership("google")