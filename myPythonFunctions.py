from random import randint
from os import remove, rename, replace
import os



# Retourner le score du joueur
#########################################################################################
def getUserPoint(username) :

    liste = []
    file = open('userScores.txt','r')
    
    for i in file.readlines() :
       liste.append(i.split())
    
    for i in range(len(liste)) :
        if liste[i][0] == username :
            file.close()
            return liste[i][1]
    file.close()
    return '-1'
#########################################################################################






# Modifier ou ajouter le score
#########################################################################################
def updateUserPoints(newuser, username, score) :
    if newuser == True :
        file = open('userScores.txt','a')
        file.write("{} {} \n".format(username, score))
        file.close()
    else :
        liste = []
        file = open('userScores.txt','r')
        with open('userScores.tmp','w') as file_tem :
            for i in file.readlines() :
                liste.append(i.split())
                
            for i in range(len(liste)) :
                if liste[i][0] == username :
                    file_tem.write(liste[i][0] + ' ' + str(score) + '\n')
                else :
                    file_tem.write(liste[i][0] + ' ' + liste[i][1] + '\n')
        file_tem.close()
        file.close()
        os.remove('userScores.txt')
        os.rename('userScores.tmp','userScores.txt')
#############################################################################################








# Generer les questions 
###############################################################################################
def genererDesQuestion() :
    operandList = [0,1,2,3,4]
    operatorList = []
    operatorDict = {1:'+',2:'-',3:'*',4:'**'}
    questionString = ''

    # Le remplissage de la liste operandList
    ##############################################################################
    for i in range(len(operandList)) :
        operandList[i] = randint(0,10)
    ##############################################################################

    # Le remplissage de la liste operatorList
    ##############################################################################
    for i in range(4) :
        index = randint(1,4)
        operatorList.append(operatorDict[index])
    for i in range(len(operatorList)-1) :
        if operatorList[i] == operatorList[i+1] == '**':
            operatorList[i+1] = operatorDict[randint(1,3)]
    ##############################################################################

    # Génerer le questionString
    ##############################################################################
    for i in range(len(operandList)) :
        if i < len(operatorList) :
            questionString = questionString + str(operandList[i]) + str(operatorList[i])
        else :
            questionString = questionString + str(operandList[i])
    ###############################################################################

    # Évaluation du résultat
    ###############################################################################
    resultat = eval(questionString)
    ###############################################################################

    # Interagir avec l'utilisateur
    ###############################################################################
    # Étape 1 :
    if '**' in questionString :
        questionString = questionString.replace("**","^")
    
    print('Question : {}'.format(questionString))

    # Étape 2 & 3 :
    while True :
        try :
            resultat_utilisateur = int(input('---> '))
            if resultat_utilisateur == resultat :
                print('Réponse Correcte')
                return 1
            else :
                print('Désolé, Fausse Réponse :/ ')
                print("La Reponse Correcte Est : {}".format(resultat))
                return 0
        except :
            print('Erreur Entrer La Réponse Correctement')
    
    ###############################################################################
#################################################################################################
