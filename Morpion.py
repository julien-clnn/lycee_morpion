 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" ****************************************************** 
    Le jeu du Morpion
    ******************************************************
    nom du fichier : TP9-exo1-julien-calonne
    auteur         : julien calonne
    date           : 20 Janvier 2020
"""

from tkinter import*
from tkinter.messagebox import*
from random import randrange
import time

#-------Forme du Morpion------#

        # 1 | 2 | 3 #
        # - + - + - #
        # 4 | 5 | 6 #
        # - + - + - #
        # 7 | 8 | 9 #
        
#--- Définition des fonctions gestionnaires d'événements : ---
#--- Couleur aléatoire ---#
def changecolor():
    #changement de couleur aléatoire de la couleur du tracé
    global coul
    pa1=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c=randrange(8)
    coul=pa1[c]
    
#--- Traçage de la grille ---#
def tableau():
    #tracer les lignes horizontales dans le cavenas can1
    changecolor()
    global x1,y1,x2,y2    
    x1,y1,x2,y2=5,5,455,5 # Coordonées de la ligne
    for i in range(0,4):
        can1.create_line(x1,y1,x2,y2,width=3,fill=coul)
        y2=y2+150
        y1=y1+150
    #tracer les lignes verticales dans le canevas can1
    global x3,y3,x4,y4
    x3,y3,x4,y4=5,5,5,455
    for i in range(0,4):
        can1.create_line(x3,y3,x4,y4,width=3,fill=coul)
        x3=x3+150
        x4=x4+150

#--- Compteur du nombre de coups joués ---#
def compteur_coup():
    global coup
    coup=coup+1

#--- Fonctions des figures (rond,croix) ---#
def rond(x,y,r,coul):
    can1.create_oval(x-r,y-r,x+r,y+r,fill=coul)

def croix(x5,y5,x6,y6,x7,y7,x8,y8,coul):
    can1.create_line(x5,y5,x6,y6,width=7,fill=coul)
    can1.create_line(x7,y7,x8,y8,width=7,fill=coul)

    
#--- Fonction Détection du CLIC ---#
def clic(position):
    global X,Y
    X=position.x
    Y=position.y
    print("position.x",position.x)
    print("position.y",position.y)
    tourjoueur()
    reperage_zone()

#--- Creation de la liste ---#
lst=[0]*10
print(lst)

#--- Assignation de la zone ---#
def reperage_zone():
    global zone
    
    if X<155:
        if Y<155:
            zone=1
        elif Y>305:
            zone=7
        else:
            zone=4
  
    elif X>305:
        if Y<155:
            zone=3
        elif Y>305:
            zone=9
        else:
            zone=6
             
    else:
        if Y<155:
            zone=2
        elif Y>305:
            zone=8
        else:
            zone=5
   
    if lst[zone]==1 or lst[zone]==2:
        showinfo(title='Probleme',message='Jouez sur une case libre')
    if lst[zone]==0:
        if joueur==1:
            lst[zone]=1
            formes()
            compteur_coup()
            test_gagnant()
            victoire1()
            victoire2()
        else:
            lst[zone]=2
            formes()
            compteur_coup()
            test_gagnant()
            victoire1()
            victoire2()
            
    
    print('Zone :',zone)
    print(lst)
    
#--- Assignation du Joueur en fonction du coup ---#
def tourjoueur():
    global joueur
    print("coup:",coup)
    if coup==0 or coup==2 or coup==4 or coup==6 or coup==8:
        joueur=1
    else:
        joueur=0
    print("joueur:",joueur)
        
#--- Creation de la figure en fonction de la zone ---#
def formes():
    if joueur==1 and coup<9:
        if zone==1:
            croix(15,15,145,145,10,145,145,10,'red')
        elif zone==2:
            croix(165,10,295,145,295,10,165,145,'red')
        elif zone==3:
            croix(315,10,445,145,445,10,315,145,'red')
        elif zone==4:
            croix(10,165,143,295,145,165,10,295,'red')
        elif zone==5:
            croix(165,165,295,295,295,165,165,295,'red')
        elif zone==6:
            croix(315,165,445,295,445,165,315,295,'red')
        elif zone==7:
            croix(10,315,145,445,145,315,10,445,'red')
        elif zone==8:
            croix(165,315,295,445,295,315,165,445,'red')
        elif zone==9:
            croix(315,315,445,445,445,315,315,445,'red')
    elif joueur==0 and coup<9:
        if zone==1:
            rond(80,80,50,'blue')
        if zone==2:
            rond(230,80,50,'blue')
        if zone==3:
            rond(380,80,50,'blue')
        if zone==4:
            rond(80,230,50,'blue')
        if zone==5:
            rond(230,230,50,'blue')
        if zone==6:
            rond(380,230,50,'blue')
        if zone==7:
            rond(80,380,50,'blue')
        if zone==8:
            rond(230,380,50,'blue')
        if zone==9:
            rond(380,380,50,'blue')
            
#--- Verification de la victoire d'un joueur ou égalité ---#
def test_gagnant():
    if lst[1]*lst[2]*lst[3]==1:
        message1()
    elif lst[4]*lst[5]*lst[6]==1:
        message1()
    elif lst[7]*lst[8]*lst[9]==1:
        message1()
    elif lst[1]*lst[4]*lst[7]==1:
        message1()
    elif lst[2]*lst[5]*lst[8]==1:
        message1()
    elif lst[3]*lst[6]*lst[9]==1:
        message1()
    elif lst[1]*lst[5]*lst[9]==1:
        message1()
    elif lst[3]*lst[5]*lst[7]==1:
        message1()
    elif lst[1]*lst[2]*lst[3]==8:
        message2()
    elif lst[4]*lst[5]*lst[6]==8:
        message2()
    elif lst[7]*lst[8]*lst[9]==8:
        message2()
    elif lst[1]*lst[4]*lst[7]==8:
        message2()
    elif lst[2]*lst[5]*lst[8]==8:
        message2()
    elif lst[3]*lst[6]*lst[9]==8:
        message2()
    elif lst[1]*lst[5]*lst[9]==8:
        message2()
    elif lst[3]*lst[5]*lst[7]==8:
        message2()
    else:
        if coup==9:
            showinfo(title='MATCH NUL',message='Aucun joueur ne gagne la partie')

#--- Messages de victoire ---#
def message1():
    showinfo(title='Victoire',message='Le joueur 1 a gagné !')
    global victoirejoueur1
    victoirejoueur1=victoirejoueur1+1
    print('Victoires du joueur 1 :',victoirejoueur1)

def message2():
    showinfo(title='Victoire',message='Le joueur 2 a gagné !')
    global victoirejoueur2
    victoirejoueur2=victoirejoueur2+1
    print('Victoires du joueur 2 :',victoirejoueur2)

#--- Affichage des victoires ---#
def victoire1():
    Affichage1.set('-> '+str(victoirejoueur1)+' <-')
    
def victoire2():
    Affichage2.set('-> '+str(victoirejoueur2)+' <-')

#--- Nouvelle Partie ---#
def retry():
    global coup,joueur,lst
    lst=[0]*10
    print(lst)
    coup=0
    joueur=0
    rond(230,230,500,'dark grey')
    tableau()


#--- Programme Principal ---#
# Les variables suivantes seront utilisées de manière globale :
coup=0
joueur=0
victoirejoueur1=0
victoirejoueur2=0

#--- Création du widget principal ("maître") ---#
fen1=Tk()
fen1.title('Jeu du Morpion')


        
#--- Création des widgets esclaves ---#
can1=Canvas(fen1,bg='dark grey',height=460,width=460)
can1.pack(side=LEFT)

#--- Création du tableau ---#
changecolor()
x1,y1,x2,y2=5,5,455,5 # Coordonées de la ligne
for i in range(0,4):
        can1.create_line(x1,y1,x2,y2,width=3,fill=coul)
        y2=y2+150
        y1=y1+150
x3,y3,x4,y4=5,5,5,455
for i in range(0,4):
        can1.create_line(x3,y3,x4,y4,width=3,fill=coul)
        x3=x3+150
        x4=x4+150
        
#--- Création de l'horloge ---#
def horloge():
    global heure,maj
    heure.set(time.strftime('%H:%M:%S'))
    fen1.after(1000,horloge)


#--- Fenetre ---#
bou1=Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)

heure= StringVar()
label0=Label(fen1,textvariable=heure,fg=coul)
label0.pack(padx=5,pady=5)
horloge()

bou2=Button(fen1,text='Changer la couleur',command=tableau)
bou2.pack()

bou3=Button(fen1,text='Recommencer',command=retry)
bou3.pack()

label1=Label(fen1,text='Victoires du joueur 1')
label1.pack()

#bou4=Button(fen1,command=victoire1)
#bou4.pack()

Affichage1= StringVar()
LabelResultat1 = Label(fen1, textvariable = Affichage1, fg ='red', bg ='white')
LabelResultat1.pack(padx = 5, pady = 5)

label3=Label(fen1,text='Victoires du joueur 2')
label3.pack()

Affichage2= StringVar()
LabelResultat2 = Label(fen1, textvariable = Affichage2, fg ='red', bg ='white')
LabelResultat2.pack(padx = 5, pady = 5)

#bou5=Button(fen1,command=victoire2)
#bou5.pack()

can1.bind("<Button-1>", clic)

fen1.mainloop() # Démarrage du réceptionnaire d'événements
fen1.destroy()  # Destruction (fermeture) de la fenêtre    

