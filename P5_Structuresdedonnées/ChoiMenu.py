import csv
import json
import xml.etree.ElementTree as AT
from mesfonction import*


with open('Donnees_Projet_Python_DataC5.csv','r',encoding='UTF-8') as csvfile:
        lect=csv.DictReader(csvfile)
        for row in lect:
            print(row)

print("----------------------MENU--------------------------")
print("1- Voulez-vous choisir les données en Csv")
print("2- Voulez-vous choisir les données en Json")
print("3- Voulez-vous choisir les données en Xml")

choix=input("choisissez un menu")
#while choix in [1,2,3]:
    #if choix==1:

            #     print(donnee)
        