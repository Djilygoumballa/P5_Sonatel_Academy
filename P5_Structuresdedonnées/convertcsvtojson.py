import csv, json
from mesfonction import*
v=[]
vi=[]
vg=[]
vig=[]

#def transJson(csv_file,json_file):
donne=[]
with open('Donnees_Projet_Python_DataC5.csv','r+') as csvfile:
    lect=csv.DictReader(csvfile)
    for row in lect:
        donne.append(row)
        #print(row)

with open('Donnees_Projet_Python_DataC5.json','w',encoding='UTF-8') as jsonfile:
    jsonfile.write(json.dumps(donne, indent=4))

for i in donne:
    i["Classe"]=i["Classe"].strip()
    for j in i["Classe"]:
        i["Classe"]=i["Classe"][0]+"em"+i["Classe"][-1]
    numero=numerovalid(i["Numero"])
    nom=nomvalid(i["Nom"])
    prenom=prevalid(i["Pr\u00e9nom"])
    date=validdate(i["Date de naissance"])
    classe=modiclas(i["Classe"])
    nott=note(i["Note"])
    if(numero==True and nom==True and prenom==True and date==True and classe==True and nott!=False):
        v.append(i)

    else:
        vi.append(i)

with open('donneesvalides.json','w',encoding='UTF-8') as validjson:
    validjson.write(json.dumps(v, indent=4))

with open('donneesinvalides.json','w',encoding='UTF-8') as invalidjson:
    invalidjson.write(json.dumps(vi, indent=4))