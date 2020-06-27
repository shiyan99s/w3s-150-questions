sample = input("Enter comma seperated numbers : ")
game1 = sample.split(",")
game2 = tuple(sample.split(","))
print("List : {}\nTuple : {}".format(game1, game2))