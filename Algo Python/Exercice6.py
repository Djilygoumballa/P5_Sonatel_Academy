#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ordre=int(input("dooner l'orde de votre matrice"))
while ordre<=4:
    ordre=int(input("donner l'ordre de votre matrice "))
choi=input("choississez votre position ['ADDP','EDDP','SDP','ADDS','EDDS','SDS']")
couleur=input("choisissez votre couleur: bleu ou rouge ou vert ")
bleu= '\033[0;34m'+'B'+'\033[0m'
rouge='\033[0;31m'+'R'+'\033[0m'
vert= '\033[0;32m'+'V'+'\033[0m'
jaune= '\033[0;33m'+'--'+'\033[0m'
rose= '\033[0;35m'+'--'+'\033[0m'

M=[]
m=[]
r=-1
for i in range(ordre):
    for j in range(ordre):
        if choi=="ADDP":
            if j>i:
                if couleur=="bleu":
                    m.append(bleu)
                elif couleur=="rouge":
                    m.append(rouge)
                elif couleur=="vert":
                    m.append(vert)
            else:
                m.append(jaune)
        elif choi=="EDDP":
            if j<i:
                if couleur=="bleu":
                    m.append(bleu)
                elif couleur=="rouge":
                    m.append(rouge)
                elif couleur=="vert":
                    m.append(vert)
            else:
                m.append(jaune)
        elif choi=="SDP":
            if j==i:
                if couleur=="bleu":
                    m.append(bleu)
                elif couleur=="rouge":
                    m.append(rouge)
                elif couleur=="vert":
                    m.append(vert)
            else:
                m.append(jaune)
                
        elif choi=="ADDS":
            if j<(ordre+r):
                if couleur=="bleu":
                    m.append(bleu)
                elif couleur=="rouge":
                    m.append(rouge)
                elif couleur=="vert":
                    m.append(vert)
            else:
                m.append(rose)
            
        elif choi=="EDDS":
            if j>(ordre+r):
                if couleur=="bleu":
                    m.append(bleu)
                elif couleur=="rouge":
                    m.append(rouge)
                elif couleur=="vert":
                    m.append(vert)
            else:
                m.append(rose)
        elif choi=="SDS":
            if j==(ordre+r):
                if couleur=="bleu":
                    m.append(bleu)
                elif couleur=="rouge":
                    m.append(rouge)
                elif couleur=="vert":
                    m.append(vert)
            else:
                m.append(rose)
    M.append(m)
    m=[]
    r+=-1
for i in M:
    for j in range(len(i)):       
        print(i[j],end="\t")
    print("\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




