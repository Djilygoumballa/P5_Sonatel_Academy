import datetime
class Etudiants:
    def __init__(self,numero,nom,prenom,datenaissance,classe,note):
        self.numero=numero
        self.nom=nom
        self.prenom=prenom
        self.datenaissance=datenaissance
        self.classe=classe
        self.note=note
 # class numerovali(Etudiant)
#  Etudiant.numero
    def numerovalid(self,numero):
        if len(self.numero)==7:
            if self.numero.isalnum()==True:
                if self.numero.isupper()==True:
                    if any(cl.isdigit() for cl in self.numero) == True:
                    
                        return self.numero
        return False
    def nomvalid(self,nom):
        cmt=0
        for i in nom:
            if self.nom[0].isalpha():
                if i.isalpha():
                    cmt=cmt+1
                    if cmt>=2:
                        return self.nom
        return  False
    
    def prenomvalid(self,prenom):
        cmt=0
        for i in prenom:
            if self.prenom[0].isalpha():
                if i.isalpha():
                    cmt=cmt+1
                    if cmt>=3:
                        return self.prenom
        return False
    def valid_date(self,datenaissance):
        try:
            self.datenaissance=self.datenaissance.strip()
            self.datenaissance=self.datenaissance.replace(' ','/').replace('-','/').replace('_','/').replace(',','/').replace('|','/').replace(':','/').replace('.','/').replace('mars','03').replace('fev','02').replace('decembre','12').replace('00','2000')
            for i in self.datenaissance:
                cl=self.datenaissance.split('/')
            if cl[0].isdigit():
                dd=int(cl[0])

            if cl[1].isdigit():
                mois=int(cl[1])
            
            if cl[2].isdigit():
                an=int(cl[2])
            d=datetime.datetime(an,mois,dd).strftime('%d/%m/%y')
            return d
        except:
            return False
    
    def validclass(self,classe):
        for i in range(len(classe)):
            self.classe=self.classe.strip()
            if self.classe[0] in ['6','5','4','3'] and self.classe[-1] in ['A','B']:
                self.classe=self.classe.strip()
                self.classe=self.classe[0]+"em"+self.classe[-1]
                return self.classe
        return False

    def validnote(self,note):
        tab=[]
        for matiere in self.note.split('#') :
            matiere=matiere.replace('[',':').replace(';',':').replace(',','.').replace(']',':').replace('|',':')
            matiere=matiere.split(":")
            del matiere[len(matiere)-1]
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
            
        return tab
