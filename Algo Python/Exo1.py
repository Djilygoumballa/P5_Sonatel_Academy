print("************************* MENU *************************\n")
t1=['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Décembre']
t2=['January','February','March','April','May','June','July','August','September','October','November','December']

print("1. Tapez 1 pour les mois en Français")
print("2. Tapez 2 pour les mois en Anglais")
print("3. Tapez 3 pour Quitter\n")

choix=int(input("Donner votre choix :"))

if choix==1:
    t= t1
elif choix==2:
    t=t2
else:
    exit()
for j in range(3):
    for i in range(j,12,3):
        if len (t[i]) < 10:
            t[i]= t[i] + (10-len(t[i]))*' '
        print (t[i],end=' | ')
    print('\n','—————————————————————————————————————————————————')