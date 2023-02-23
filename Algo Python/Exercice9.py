#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sais(z):
    No=int(input("donner le nombre d'opérateurs "))
    for i in range(No):
        opera=input("donner un opérateur ")
        z.append(opera)
    nc=int(input("donner le nombre de clients "))
    for i in range(nc):
        nom=input("donner le nom du client ")
        prenom=input("donner le prenom du client ")
        numero=input("donner le numero du client ")
        p=vn(numero)
        while p==False:
            numero=input("saississez un bon numero svp ")
            p=vn(numero)
        z.append([prenom,nom,numero])
def affiche(t):
    for i in t:
        if i=='orange':
            print(i)
            for j in t:
                for k in j:
                    if len(k)==9 and k[0]=='7' and (k[1]=='7' or k[1]=='8'):
                        for c in range(len(j)):
                            print(j[c],end=("\t"))
                        print("\n")
        elif i=='free':
            print(i)
            for j in t:
                for k in j:
                    if len(k)==9 and k[0]=='7' and k[1]=='6':
                        for c in range(len(j)):
                            print(j[c],end=("\t"))
                        print("\n")
        elif i=='expresso':
            print(i)
            for j in t:
                for k in j:
                    if len(k)==9 and k[0]=='7' and k[1]=='0':
                        for c in range(len(j)):
                            print(j[c],end=("\t"))
                        print("\n")
        elif i=='Promobile':
            print(i)
            for j in t:
                for k in j:
                    if len(k)==9 and k[0]=='7' and k[1]=='5':
                        for c in range(len(j)):
                            print(j[c],end=("\t"))
                        print("\n")
def aff(a,b):
    print(a)
    if a=='orange':
        for j in b:
            for k in j:
                if len(k)==9 and k[0]=='7' and (k[1]=='7' or k[1]=='8'):
                    for c in range(len(j)):
                        print(j[c],end=("\t"))
                    print("\n")
    elif a=='free':
        for j in b:
            for k in j:
                if len(k)==9 and k[0]=='7' and k[1]=='6':
                    for c in range(len(j)):
                        print(j[c],end=("\t"))
                    print("\n")
    elif a=='expresso':
        for j in b:
            for k in j:
                if len(k)==9 and k[0]=='7' and k[1]=='0':
                    for c in range(len(j)):
                        print(j[c],end=("\t"))
                    print("\n")
    elif a=='Promobile':
        for j in b:
            for k in j:
                if len(k)==9 and k[0]=='7' and k[1]=='0':
                    for c in range(len(j)):
                        print(j[c],end=("\t"))
                    print("\n")
def vn(a):
    nb=["0","1","2","3","4","5","6","7","8","9"]
    Si=["0","5","6","7","8"]
    tab=[]
    s=''
    for i in range(len(a)):
        if a[i] in nb:
            s+=a[i]
    tab.append(s)
    
    for num in tab:
        if len(num)!=9 or num[0]!='7' or num[1] not in Si:
            return False
        else:
            return True

def affnum(prenom,nom,tab):
    print("les numéros de ",prenom,nom,"sont:")
    for z in tab:
        if prenom in z and nom in z:
            print(z[2],end="|")
        print("\n")
            
def modnum(prenom,nom,tab):
    bol = False
    for cl in tab:
        if prenom in cl and nom in cl:
            bol = True
            choix=input("voulez-vous ajouter,modifier un numéro d'un client ou non ")
            if choix=='ajouter':
                i=0
                if i < 1:
                    nom=nom
                    prenom=prenom
                    numero=input("entrez le nouveau numero ")
                    p=vn(numero)
                    while p==False:
                        numero=input("saississez un bon numero svp ")
                        p=vn(numero)
                    tab.append([prenom,nom,numero])
                    i+=1
                elif i>=1:
                    choix=input("voulez vous ajouter un autre numero oui ou non ")
                    if choix=='oui':
                        nom=nom
                        prenom=prenom
                        numero=input("entrez le nouveau numero ")
                        p=vn(numero)
                        while p==False:
                            numero=input("saississez un bon numero svp ")
                            p=vn(numero)
                        tab.append([prenom,nom,numero])
                        i+=1
                    else:
                        break
            elif choix == 'modifier':
                i=0
                if i < 1:
                    numero=input("donner le  nouveau numero du client ")
                    p=vn(numero)
                    while p==False:
                        numero=input("saississez un bon numero svp ")
                        p=vn(numero)
                    cl[2]=numero
                    i+=1
                elif i>=1:
                    choix=input("voulez vous modifier l'autre numero oui ou non ")
                    if choix=='oui':
                        numero=input("donner le numero du client ")
                        p=vn(numero)
                        while p==False:
                            numero=input("saississez un bon numero svp ")
                            p=vn(numero)
                        cl[2]=numero
                        i+=1
                    else:
                        break
            elif choix == 'non':
                
                break
                
        else:
            bol = False
            
    if bol == False:
                print("pas dans le tableau")


tab=[]
print("----------------------MENU--------------------------")
print("1-Saisie du tableau")
print("2-Affichage complet des clients")
print("3-Affichage des clients d'un opérateur")
print("4-Affichage des numeros d'un client")
print("5-Ajout ou modification des numeros d'un client")
print("6-sortir du programme")
choix=int(input("choissiez un menu"))
while choix in[1,2,3,4,5]:
    if choix==1:
        sais(tab)
    elif choix==2:
        affiche(tab)
    elif choix==3:
        x=input("quel opérateur voulez-vous choisir")
        aff(x,tab)
    elif choix==4:
        p=input("le prenom")
        N=input("le nom")
        affnum(p,N,tab)
    elif choix==5:
        p=input("le prenom")
        N=input("le nom")
        modnum(p,N,tab)
    print("----------------------MENU--------------------------")
    print("1-Saisie du tableau")
    print("2-Affichage complet des clients")
    print("3-Affichage des clients d'un opérateur")
    print("4-Affichage des numeros d'un client")
    print("5-Ajout ou modification des numeros d'un client")
    print("6-sortir du programme")
    choix=int(input("choissiez un menu  "))  

if choix==6:
    exit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




