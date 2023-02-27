import datetime

#focntion qui permet de verifier la validité des numeros

def numerovalid(numero):
    if len(numero)==7:
        if numero.isalnum()==True:
            if numero.isupper()==True:
                    if any(cl.isdigit() for cl in numero) == True:
                    
                        return True,numero
    return "le numero n'est pas valide"
print(numerovalid("GFD3G8G"))

##focntion qui permet de verifier la validité des prenom
def prevalid(prenom):
    cmt=0
    for i in prenom:
        if prenom[0].isalpha():
            if i.isalpha():
                cmt=cmt+1
                if cmt>=3:
                    return True
    return False

#focntion qui permet de verifier la validité des noms    
def nomvalid(nom):
    cmt=0
    for i in nom:
        if nom[0].isalpha():
            if i.isalpha():
                cmt=cmt+1
                if cmt>=2:
                    return True
    return  False

#focntion qui permet de modifier les classes
def modiclas(classe):
    for i in range(len(classe)):
        classe=classe.strip()
        if classe[0] in ['6','5','4','3'] and classe[-1] in ['A','B']:
            classe=classe.strip()
            classe=classe[0]+"em"+classe[-1]
            return True
        return False

    
def validdate(date):
    try:
        for i in date:
            if i==" ":
                date.remove(i)
        date=date.strip()
        date=date.replace(' ','/').replace('-','/').replace('_','/').replace(',','/').replace('|','/').replace(':','/').replace('.','/').replace('mars','03').replace('fev','02').replace('decembre','12').replace('00','2000')
        cl=date.split('/')
        if cl[0].isdigit():
            dd=int(cl[0])

        if cl[1].isdigit():
            mois=int(cl[1])
        
        if cl[2].isdigit():
            an=int(cl[2])
        d=datetime.datetime(an,mois,dd).strftime('%d/%m/%y')
        return True
    except:
        return False


nt="Math[11|13:06] #Francais[08|17:12] #Anglais[13|13:12] #PC[09|18:07] #SVT[15|10:10] #HG[14|19:17]"
def note(a):
    # print(a)
    tab=[]
    for matiere in a.split('#') :
        matiere=matiere.replace('[',':').replace(';',':').replace(',','.').replace(']',':').replace('|',':')
        matiere=matiere.split(":")
        del matiere[len(matiere)-1]
        # print("dd",matiere)
        s=0
        nbr=0
        moy=1
        mm=0
        d=0
        if matiere==""  or matiere==" " or len(matiere)<= 1:
            return False   
        for i in range (1,len(matiere)):
            for c in matiere[i]:
                if c not in["0","1","2","3","4","5","6","7","8","9","."]:
                    return False
        for j in range(len(matiere)):
            if matiere[j]=="" or matiere[j]==" ":
                matiere[j]=matiere[j].replace("",'0.0').replace(" ",'0.0')
        for j in range (1,len(matiere)-1):
            s+=float(matiere[j])
            nbr+=1
        moy=round(((s/nbr)+2*float(matiere[-1]))/3,2)
        if (moy) > 0 and (moy) <=20:
            matiere.append(moy)
            tab.append(matiere)
            # tab.append(moygen)
    return tab
#print(note(nt))


def recher(s,tab):

    lo=False
    for stu in tab:
        if s in stu:
            lo=True
            for w in range (len(stu)):
                print(stu[w],end=(13-len(str(stu[w])))*' ')
            print("\n")
    if lo==False:
        print("l'etudiant n'est pas sur la liste")

def ajouter(a):
    code=str(input("saissez le code de l'etudiant"))
    numero=str(input("saissez le numero"))
    num=numerovalid(numero)
    while num==False:
        numero=str(input("saissez le bon numero"))
        num=numerovalid(numero)
    nom=str(input("saissez le nom"))
    no=nomvalid(nom)
    while no==False:
        nom=str(input("saissez le bon nom"))
        no=nomvalid(nom)
    prenom=str(input("saissez le prenom"))
    pre=prevalid(prenom)
    while pre==False:
        prenom=str(input("saissez le bon prenom"))
        pre=prevalid(prenom)
    datedenaissance=str(input("saissez la date de naissance"))
    dat=validdate(datedenaissance)
    while dat==False:
        datedenaissance=str(input("saissez la bonne date de naissance"))
        dat=validdate(datedenaissance)
    classe=str(input("saissez la classe"))
    cla=modiclas(classe)
    while cla==False:
        classe=str(input("saissez la bonne classe"))
        cla=modiclas(classe)
    
    # notes=(input("saissez des matières séparés par des # et leurs notes par des :"))
    # noo=note(notes)
    # while noo==False:
    #     notes=(input("saissez des matières séparés par des # et leurs notes par des : "))
    #     noo=note(notes)
        
    a.append([code,numero,nom,prenom,datedenaissance,classe,])