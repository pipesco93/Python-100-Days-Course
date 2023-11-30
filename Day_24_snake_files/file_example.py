with open("my_file.txt", mode="a") as file: #If I don't specify a mode it would be read only
    #if I try to open a file that does not exist, it will create one

    # contents = file.read()
    # print(contents)

    file.write("\nNew text 2")


    #file.close()   If I use with to open hte file i don't have to close it