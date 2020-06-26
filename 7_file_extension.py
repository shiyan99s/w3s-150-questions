filename = input("Enter file name with extn = ")
file_list = filename.split(".")
file_extn = file_list[-1]
print("file extension = {}".format(file_extn))