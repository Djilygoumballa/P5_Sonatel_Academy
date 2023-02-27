import csv
import xml.etree.ElementTree as AT
from mesfonction import*

donne=[]
with open('Donnees_Projet_Python_DataC5.csv','r+',encoding='UTF-8') as csvfile:
    lect=csv.DictReader(csvfile)
    for row in lect:
        donne.append(row)
qs=""
for i in donne:

    ch= '''
        <Etudiant>
                <Code>%s</Code>
                <Numero>%s</Numero>
                <Nom>%s</Nom>
                <Prenom>%s</Prenom>
                <Date_de_naissance>%s</Date_de_naissance>
                <Classe>%s</Classe>
                <Note>%s</Note>
        </Etudiant>
    ''' % (i["CODE"],i["Numero"],i["Nom"],i["Prénom"],i["Date de naissance"],i["Classe"],i["Note"])
    qs+=ch

with open('Donnees_Projet_Python_DataC5.xml','w') as filexml:
    filexml.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no' ?>\n <ETUDIANTS>")
    filexml.write(qs)
    filexml.write("\n</ETUDIANTS>")

v=[]
vi=[]

for i in donne:
    dico={}
    i["Classe"]=i["Classe"].strip()
    for j in i["Classe"]:
        i["Classe"]=i["Classe"][0]+"em"+i["Classe"][-1]
    numero=numerovalid(i["Numero"])
    nom=nomvalid(i["Nom"])
    prenom=prevalid(i["Prénom"])
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
ds=""
for i in v:
    vld='''
            <Etudiant>
                <Code>%s</Code>
                <Numero>%s</Numero>
                <Nom>%s</Nom>
                <Prenom>%s</Prenom>
                <Date_de_naissance>%s</Date_de_naissance>
                <Classe>%s</Classe>
                <Note>%s</Note>
            </Etudiant>
        ''' % (i["CODE"],i["Numero"],i["Nom"],i["Prénom"],i["Date de naissance"],i["Classe"],i["Note"])
    ds+=vld

with open('Donnees_valides.xml','w') as validsxml:
    validsxml.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no' ?>\n <ETUDIANTS>")
    validsxml.write(ds)
    validsxml.write("\n</ETUDIANTS>")

ml=""
for i in vi:
    pol='''
            <Etudiant>
                <Code>%s</Code>
                <Numero>%s</Numero>
                <Nom>%s</Nom>
                <Prenom>%s</Prenom>
                <Date_de_naissance>%s</Date_de_naissance>
                <Classe>%s</Classe>
                <Note>%s</Note>
            </Etudiant>
        ''' % (i["CODE"],i["Numero"],i["Nom"],i["Prénom"],i["Date de naissance"],i["Classe"],i["Note"])
    ml+=pol

with open('Donnees_invalides.xml','w') as invalidsxml:
    invalidsxml.write("<?xml version='1.0' encoding='ISO-8859-1' standalone='no' ?>\n <ETUDIANTS>")
    invalidsxml.write(ml)
    invalidsxml.write("\n</ETUDIANTS>")
    
