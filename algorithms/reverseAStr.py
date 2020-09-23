def revStr ():

    string = input("enter a string and it will be reverse \n: ")
    emptyArr = []
    for char in string:
        emptyArr.insert(0, char)
        # print(emptyArr)
    print("".join(emptyArr))
revStr()



