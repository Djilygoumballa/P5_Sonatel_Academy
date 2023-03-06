import csv
from fonctionPOO import *
from tabulate import tabulate
lect=open("Donnees_Projet_Python_DataC5.csv")
df=csv.reader(lect)
vdg=[]
vd=[]
vi=[]
vig=[]
for dt in df:

    numero_etu = Etudiants(dt[1],dt[2],dt[3],dt[4],dt[5],dt[6])
    numero=numero_etu.numerovalid(dt[1])
    nom=numero_etu.nomvalid(dt[2])
    prenom=numero_etu.prenomvalid(dt[3])
    datenaiss=numero_etu.valid_date(dt[4])
    cla=numero_etu.validclass(dt[5])        
    nott=numero_etu.validnote(dt[6])

    if (numero!=False and nom!=False and prenom!=False and datenaiss!=False and cla!=False and nott!=False):
        vd.append(dt[1])
        vd.append(dt[2])
        vd.append(dt[3])
        vd.append(datenaiss)
        vd.append(dt[5])
        vd.append(nott)
        vdg.append(vd)
        vd=[]
    
    else:
        vi.append(dt[1])
        vi.append(dt[2])
        vi.append(dt[3])
        vi.append(datenaiss)
        vi.append(dt[5])
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
choix=int(input("choisissez un menu"))
while choix in[1,2,3,4,5,]:
    if choix==1:
        ch=input("choisir les informations à afficher: valides ou invalides: ")
        if ch== "valides":
            print(tabulate(vdg,headers=['Numero','Nom','Prénom','Date de naissance','Classe','Note']))
            # for i in vdg:
            #     for j in range (len(i)):
            #         print(i[j],end=(15-len(i[j]))*' ')
            #     print("\n")
            # print(len(vdg))
        elif ch== "invalides":
            print(tabulate(vi,headers=['Numero','Nom','Prénom','Date de naissance','Classe','Note']))
            for i in vi:
                print(i)
            print("\n")
        else:
            print("Regardez bien votre choix")
