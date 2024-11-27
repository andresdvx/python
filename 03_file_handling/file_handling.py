try:
    file = open('../myFile.txt', "r") # open file in read mode
    print(file.read()) # read file to print
except Exception as e:
    print(e)