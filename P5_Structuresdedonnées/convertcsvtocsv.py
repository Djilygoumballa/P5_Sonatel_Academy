import csv
from mesfonction import*
v=[]
vi=[]

donne=[]
with open('Donnees_Projet_Python_DataC5.csv','r+',encoding='UTF-8') as csvfile:
    lect=csv.DictReader(csvfile)
    for row in lect:
        donne.append(row)

for i in donne:
    dico={}
    i["Classe"]=i["Classe"].strip()
    numero=numerovalid(i["Numero"])
    nom=nomvalid(i["Nom"])
    prenom=prevalid(i["Pr\u00e9nom"])
    date=validdate(i["Date de naissance"])
    classe=modiclas(i["Classe"])
    nott=note(i["Note"])
    dico["CODE"]=i["CODE"]
    dico["Numero"]=i["Numero"]
    dico["Nom"]=i["Nom"]
    dico["Prénom"]=i["Prénom"]
    dico["Date de naissance"]=i["Date de naissance"]
    dico["Classe"]=i["Classe"]   
    dico["Note"]=nott
    if(numero==True and nom==True and prenom==True and date==True and classe==True and nott!=False):
        v.append(dico)

    else:
        vi.append(dico)
#print(v)
#headers=['CODE', 'Numero', 'Nom', 'Prénom', 'Date de naissance', 'Classe', 'Note']
with open('donneesvalides.csv', 'w',encoding='UTF-8') as validcsv:    
    bindeu=csv.DictWriter(validcsv,delimiter=',',fieldnames=['CODE', 'Numero', 'Nom', 'Prénom', 'Date de naissance', 'Classe', 'Note'])
    bindeu.writerows(v)


with open('donneesinvalides.csv', 'w',encoding='UTF-8') as invalidcsv:
    bindeu=csv.DictWriter(invalidcsv,delimiter=',',fieldnames=['CODE', 'Numero', 'Nom', 'Prénom', 'Date de naissance', 'Classe', 'Note'])
    bindeu.writerows(vi)
