#!/usr/bin/env python
# coding: utf-8

# In[40]:


ch=input("donner des numeros separés par des - et a la fin aussi")
N=""
tabN=[]
NB=["0","1","2","3","4","5","6","7","8","9"]
for i in range(len(ch)):
    if ch[i]==" ":
        continue
    if ch[i]!="-":
         N+=ch[i]
    else:
        tabN.append(N)

numvali=[]
numval=[]
numinva=[]
numero=""
for numero in tabN:
    if len(numero)!=9:
        numinva.append(numero) 
    else:
        numval.append(numero)


for sc in numval:
    for i in sc:
        if i not in NB:
            numval.remove(sc)
            numinva.append(sc)

operateur=['77','78','70','75','76']
vi=''
numnor=[]
orange=0
free=0
expresso=0
Promobile=0
for vi in numval:
    id=vi[0]+vi[1]
    if id in operateur:
        numnor.append(vi)
    if id=='77' or id=='78':   
        orange+=1
    elif id=='76':
        free+=1
    elif id=='70':
        expresso+=1
    elif id==75:
        Promobile+=1

for elt in numval:
    for el in numinva:

        print(elt,"\t\t",el)
  


# In[ ]:





# In[ ]:




