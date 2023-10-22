import requests
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
from random import choice
from csv import DictWriter, DictReader

def writetofile(lista, file):
    with open(file, "w") as f:
        for item in lista:
            f.write(item + "\n");
    f.close()
    
    
def valid(lista):
    l = lista.split(" ")
    for k in l:
        if( int(k) > 39):
            return False
    return True

def scrape(izvlacnje, godinu):
    res = requests.get("https://www.lutrija.rs/Results?drawNo="+izvlacnje+"&gameNo=1&drawYear="+godinu)
    soup = BeautifulSoup(res.text, "html.parser")
    rezultati = [el.text for el in soup.find_all("div", class_="Rez_Brojevi_Txt_Gray")]
    return [" ".join(rezultati[:7]), " ".join(rezultati[7:14]), " ".join(rezultati[14:20])]

    
def sva_izvlacenja():
    
    i=108
    g=2011
    loto = []
    lotoplus = []
    dzoker = []
    while(g > 2010):
        while(i > 0):
            print(f"kolo {i}; godina {g}")     
            c, cplus, dz = scrape(str(i),str(g))
            print(f"{c} - {cplus} - {dz}")
            if(valid(c)):
                loto.append(c)
                lotoplus.append(cplus)
                dzoker.append(dz) 
            i-=1
            # print(loto)
            # print(lotoplus)
            # print(dzoker)
        i=107
        g-=1 
    
    loto_file = f"./rez/loto{g}.txt"
    loto_plus_file = f"./rez/loto_plus{g}.txt"
    dzoker_file = f"./rez/dzoker{g}.txt"
    writetofile( loto, loto_file)
    writetofile( lotoplus, loto_plus_file)
    writetofile( dzoker, dzoker_file)


sva_izvlacenja()

# l = ["fasfasfasf", "fasfasfasfas", "Fasfasfasfas"]

# writetofile(l, "./rez/testfaj")