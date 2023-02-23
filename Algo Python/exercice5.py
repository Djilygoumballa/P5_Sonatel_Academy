#!/usr/bin/env python
# coding: utf-8

# In[23]:


ordre=int(input("donner l'ordre de votre matrice "))
while ordre<=5:
    ordre=int(input("donner l'ordre de votre matrice "))

couleur=input("choisissez votre couleur: bleu ou rouge ")
choi=input("choisissez votre position: haut ou bas ")
mat=[]
A=[]
bleu= '\033[0;34m'+'C'+'\033[0m'
rouge='\033[0;31m'+'C'+'\033[0m'
for i in range(ordre):
    for j in range(ordre):
        if j>i and choi=="haut":
            if couleur=="bleu":
                A.append(bleu)
            elif couleur=="rouge":
                A.append(rouge)
        elif j<i and choi=="bas":
            if couleur=="bleu":
                A.append(bleu)
            elif couleur=="rouge":
                A.append(rouge)
        else:
            A.append("-")
    
    mat.append(A)
    A=[]
for m in mat:
    for i in range(len(m)):       
        print(m[i],end="\t")
    print("\n")


# In[ ]:





# In[ ]:





# In[ ]:




