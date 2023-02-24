import csv
from tabulate import tabulate
from datetime import datetime
from mesfonction import *


vdg=[]
vd=[]
vig=[]
vi=[]
with open('Donnees_Projet_Python_DataC5.csv','r+') as f:
    lect=csv.reader(f)
    for i in lect:
        #infos=["Code","Numero","Nom","Prenom","Date de Naissance","Classe","Note"]
    #print(infos)
        i[6]=i[6].strip()
        i[6]=i[6].replace('"','').replace(' ','')
        #print(i[6])
        i[5]=i[5].strip()
        for j in i[5]:
            i[5]=i[5][0]+"em"+i[5][-1]
            #print(i[5])
        numero=numerovalid(i[1])
        nom=nomvalid(i[2])
        prenom=prevalid(i[3])
        date=validdate(i[4])
        #print(date)
        classe=modiclas(i[5])
        nott= note(i[6])
        #print(nott)
        if (numero==True and nom==True and prenom==True and date==True and classe==True and nott!=False):   
            #vd.append(infos)
            vd.append(i[1])
            vd.append(i[2])
            vd.append(i[3])
            vd.append(i[4])
            vd.append(i[5])
            vd.append(nott)
            vdg.append(vd)
            vd=[]

            
        else:
            vi.append(i[1])
            vi.append(i[2])
            vi.append(i[3])
            vi.append(i[4])
            vi.append(i[5])
            vi.append(nott)   
            vig.append(vi)
            vi=[]
            


print("----------------------MENU--------------------------")
print("1-afficher les informations: ")
print("2-afficher une information (par son numéro)")
print("3-ajouter une information en vérifiant la validité des informations données")
print("4-afficher les cinq premiers")
print("5-modifier une information invalide ensuite le transférer dans la structure où se trouve les informations valides")
print("6-sortir du programme")
choix=int(input("choissiez un menu"))
while choix in[1,2,3,4,5,]:
    if choix==1:
        ch=input("choisir les informations à afficher: valides ou invalides: ")
        if ch== "valides":
            print(tabulate(vdg,headers=['Numero','Nom','Prénom','Date de naissance','Classe','Note']))
            # for i in vdg:
            #     for j in range (len(i)):
            #         print(i[j],end=(15-len(i[j]))*' ')
            #     print("\n")
            #     #print(len(vdg))
        elif ch== "invalides":
            print(tabulate(vig,headers=['Numero','Nom','Prénom','Date de naissance','Classe','Note']))
            # for i in vig:
            #     print(i)
            # print("\n")
        else:
            print("Regardez bien votre choix")

    elif choix==2:
        B=input("entrez le numero de l'etudiant")
        recher(B,vdg)
    elif choix==3:
        ajouter(vdg)
    print("----------------------MENU--------------------------")
    print("1-afficher les informations: ")
    print("2-afficher une information (par son numéro)")
    print("3-afficher les cinq premiers")
    print("4-ajouter une information en vérifiant la validité des informations données")
    print("5-modifier une information invalide ensuite le transférer dans la structure où se trouve les informations valides")
    print("6-sortir du programme")
    choix=int(input("choissiez un menu  "))
        
