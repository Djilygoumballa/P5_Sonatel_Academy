#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Essai8 import*

tab = [['Prenom', 'Nom', 'Telephone', 'Classe','Devoir', 'Projet', 'Examen', 'Moyenne']]

print("---------------Choisissez un numero par rapport au Menu---------------")
print("1.Ajouter des etudiants ")
print("2.Afficher des etudiants")
print("3.Trier les etudiants par moyenne")
print("4.Rechercher un etudiant par son telephone")
print("5.Modifier les notes d'un etudiant")
print("6.Quitter")
choix = int(input("Choissisez un menu : "))
while choix in [1, 2, 3, 4, 5]:
    if choix == 1:
        saisie(tab)
    elif choix == 2:
        afficher(tab)
    elif choix == 3:
        tri(tab)
    elif choix == 4:
        b=input("entrez le numero de telephone de l'etudiant ")
        recher(b,tab)
    elif choix == 5:
        g=input("modification des notes: entrez son numero de telephone")
        mn(g,tab)

    print("---------------Choisissez un numero par rapport au Menu---------------")
    print("1.Ajouter des etudiants ")
    print("2.Afficher des etudiants")
    print("3.Trier les etudiants par moyenne")
    print("4.Rechercher un etudiant par son telephone")
    print("5.Modifier les notes d'un etudiant")
    print("6.Quitter")

    choix = int(input("Choissisez un menu : "))

if choix == 6:
    exit()


# In[ ]:





# In[ ]:




