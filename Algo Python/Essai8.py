#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def saisie(a):
    Prénom=str(input("saissisez le prénom :"))
    Nom=str(input("saissisez le nom :"))
    Telephone=str(input("saissisez le numéro de telephone :"))  
    bol=vn(Telephone)
    while bol== False:
            Telephone=str(input("saissisez le bon numéro de telephone svp :"))
            bol=bol=vn(Telephone)
    Classe=str(input("saissisez la classe :"))
    Devoir=float(input("saississez la note de devoir :"))
    dev=note(Devoir)
    while dev==False:
        Devoir=float(input("saississez la bonne note de devoir svp :"))
        dev=note(Devoir)
    Examen=float(input("saississez la note d'examen :"))
    exam=note(Examen)
    while exam==False:
        Examen=float(input("saississez la bonne note d'examen svp :"))
        exam=note(Examen)
    Projet=float(input("saississez la note de projet"))
    pro=note(Projet)
    while pro==False:
        Projet=float(input("saississez la bonne note de projet svp :"))
        pro=note(Projet)
    Moyenne=(moy(Devoir,Examen,Projet))
    a.append([Prénom,Nom,Telephone,Classe,Devoir,Examen,Projet,Moyenne])
    
    choix=input("voulez vous taper un autre étudiant oui ou non")
    while choix=='oui':
            Prénom=str(input("saissisez le prénom"))
            Nom=str(input("saissisez le nom"))
            Telephone=str(input("saissisez le numéro de telephone"))  
            bol=vn(Telephone)
            while bol== False:
                    print("resaissez un bon numéro svp")
                    Telephone=str(input("saissisez le numéro de telephone"))
                    bol=bol=vn(Telephone)
            Classe=str(input("saissisez la classe"))
            Devoir=float(input("saississez la note de devoir"))
            dev=note(Devoir)
            while dev==False:
                print("saissez la note de devoir")
                Devoir=float(input("saississez la note de devoir"))
                dev=note(Devoir)
            Examen=float(input("saississez la note d'examen"))
            exam=note(Examen)
            while exam==False:
                print("saississez la note d'examen")
                Examen=float(input("saississez la note d'examen"))
                exam=note(Examen)
            Projet=float(input("saississez la note de projet"))
            pro=note(Projet)
            while pro==False:
                print("saississez la note de projet")
                Projet=float(input("saississez la note de projet"))
                pro=note(Projet)
            Moyenne=moy(Devoir,Examen,Projet)
            a.append([Prénom,Nom,Telephone,Classe,Devoir,Examen,Projet,Moyenne])

            choix=input("voulez vous taper un autre étudiant oui ou non")
    

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
        
def note(N):
    if N< 0 or N>20:
        return False
    else:
        return True
def moy(a,b,c):
    moyenne=(a+b+c)/3
    return moyenne

def afficher(B):
    print(114 * '*')
    for j in B:
        for i in range(len(j)):
            print("|",j[i],end=(13-len(str(j[i])))*' ')
        print("\n")
    print(114 * '*')
    
def recher(s,tab):
    lo=False
    for stu in tab:
        if s in stu:
            lo=True
            for w in range (len(stu)):
                print("|",stu[w],end=(13-len(str(stu[w])))*' ')
            print("\n")
    if lo==False:
        print("l'etudiant n'est pas saur la liste")
        
def mn(q,tab):
    lel=False
    for f in tab:
        if q== f[2]:
            lel=True
            Devoir=float(input("saississez la note de devoir :"))
            dev=note(Devoir)
            while dev==False:
                Devoir=float(input("saississez la bonne note de devoir svp :"))
                dev=note(Devoir)
            Examen=float(input("saississez la note d'examen :"))
            exam=note(Examen)
            while exam==False:
                Examen=float(input("saississez la bonne note d'examen svp :"))
                exam=note(Examen)
            Projet=float(input("saississez la note de projet"))
            pro=note(Projet)
            while pro==False:
                Projet=float(input("saississez la bonne note de projet svp :"))
                pro=note(Projet)
            Moyenne=moy(Devoir,Examen,Projet)
            f[4] = Devoir
            f[5] = Examen
            f[6] = Projet
            f[7] = Moyenne
            for h in range (len(f)):
                print("|",f[h],end=(13-len(str(f[h])))*' ')
            print("\n")
    if lel==False:
        print("le numero que vous avez donné n'est pas sur la liste")
        
def tri(tab):
    for i in range(2, len(tab)):
        k = tab[i]
        j = i-1
        a = tab[j]
        m = k[len(k)-1]
        n = a[len(a)-1]
        while j >= 1 and m > n:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = k
    print("le tableau trié  \n")
    afficher(tab)


# In[ ]:





# In[ ]:




