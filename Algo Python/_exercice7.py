#!/usr/bin/env python
# coding: utf-8

# In[1]:


chaine=input("ecrivez une phrase: ")

N=""
t=[]
tab=[]
for i in chaine:
    if i=='0':
        t.append('A')
    elif i=="'":
        t.append("'")
    elif i=='1':
        t.append('B')
    elif i=='2':
        t.append('C')
    elif i=='3':
        t.append('D')
    elif i=='4':
        t.append('E')
    elif i=='5':
        t.append('F')
    elif i=='6':
        t.append('G')
    elif i=='7':
        t.append('H')
    elif i=='8':
        t.append('I')
    elif i=='9':
        t.append('J')
    elif i==' ':
        t.append('00')
    elif i=='A' or i=='a':
        t.append('2')
    elif i=='B' or i=='b':
        t.append('22')
    elif i=='C' or i=='c':
        t.append('222')
    elif i=='D' or i=='d':
        t.append('3')
    elif i=='E' or i=='e':
        t.append('33')
    elif i=='F' or i=='f':
        t.append('333')
    elif i=='G' or i=='g':
        t.append('4')
    elif i=='H' or i=='h':
        t.append('44')
    elif i=='I' or i=='i':
        t.append('444')
    elif i=='J' or i=='j':
        t.append('5')
    elif i=='k' or i=='k':
        t.append('55')
    elif i=='L' or i=='l':
        t.append('555')
    elif i=='M' or i=='m':
        t.append('6')
    elif i=='N' or i=='n':
        t.append('66')
    elif i=='O' or i=='o':
        t.append('666')
    elif i=='P' or i=='p':
        t.append('7')
    elif i=='Q' or i=='q':
        t.append('77')
    elif i=='R' or i=='r':
        t.append('777')
    elif i=='S' or i=='s':
        t.append('7777')
    elif i=='T' or i=='t':
        t.append('8')
    elif i=='U' or i=='u':
        t.append('88')
    elif i=='V' or i=='v':
        t.append('888')
    elif i=='W' or i=='w':
        t.append('9')
    elif i=='X' or i=='x':
        t.append('99')
    elif i=='Y' or  i=='y':
        t.append('999')
    elif i=='Z' or i=='z':
        t.append('9999')
#for i in t:
tab.append(t[0])
for j in range(1, len(t)):
        phr=t[j-1]
        hp=t[j]
        if phr[len(phr)-1]==hp[0]:
            tab.append('0')
        tab.append(t[j])
#print(t)
#print(tab)
for i in tab:
    print(i,end="")


# In[ ]:




