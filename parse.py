def givedic(filename):
        
    diclist = {}
    with open(filename, "r") as file:
        for line in file:
            if line != "\n":
                z = line.strip()
                diclist[z] =  diclist[z]+1 if z in diclist else 1
    
    file.close()
    print(diclist)
    return diclist

