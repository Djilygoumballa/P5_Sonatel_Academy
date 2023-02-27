import csv, json
import xml.etree.ElementTree as AT
from mesfonction import*
v=[]
vi=[]
vg=[]
vig=[]

#def transJson(csv_file,json_file):
donne=[]
with open('Donnees_Projet_Python_DataC5.csv','r+',encoding='UTF-8') as csvfile:
    lect=csv.DictReader(csvfile)
    for row in lect:
        donne.append(row)
        #print(row)

with open('Donnees_Projet_Python_DataC5.json','w',encoding='UTF-8') as jsonfile:
    jsonfile.write(json.dumps(donne, indent=4))

for i in donne:
    dico={}
    i["Classe"]=i["Classe"].strip()
    for j in i["Classe"]:
        if i["Classe"][0] in ['6','5','4','3'] and i["Classe"][-1] in ['A','B']:
            i["Classe"]=i["Classe"][0]+"em"+i["Classe"][-1]
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

with open('donneesvalides.json','w',encoding='UTF-8') as validjson:
    validjson.write(json.dumps(v, indent=4))

with open('donneesinvalides.csv','w',encoding='UTF-8') as invalidjson:
    invalidjson.write(json.dumps(vi, indent=4))