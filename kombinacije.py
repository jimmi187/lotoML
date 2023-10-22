def givedicsorted(filename):
    ret = []
    diclist = {}
    with open(filename, "r") as file:
        for line in file:
            if line != "\n":
                z = line.strip().split(" ")
                if "8" in z and "23" in z and "37" in z :
                    ret.append(z)         
                for c in z:
                    diclist[c] = diclist[c]+1 if c in diclist else 1
    file.close()
    # for x , y in diclist:
    #     diclist2[y] = x 
    sorted_dict = dict(sorted(diclist.items(), key=lambda item: item[1]))
    print(sorted_dict)  
    return ret
def givecomb(filename):
    diclist = {}
    with open(filename, "r") as file:
        for line in file:
            if line != "\n":
                c = line.strip()
                diclist[c] = diclist[c]+1 if c in diclist else 1
    file.close()
    sorted_dict = dict(sorted(diclist.items(), key=lambda item: item[1]))
    print(sorted_dict)  
    
file = ".\\rez\\lotozbir"
file2 = ".\\rez\\lotopluszbir"
file3 = ".\\rez\\ukupno"
file4 = ".\\rez\\ukupDzo"
givecomb(file)

k = givedicsorted(file)

print(k)