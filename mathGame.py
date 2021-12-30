from myPythonFunctions import *





# Le programme principal
######################################################################################################################
if __name__== '__main__' :
    try :
        userChoice = 0
        print('################################### Bienvenue ###################################')
        print()
        print('Entrer Votre Nom : ')
        username = input('----> ')
        userscore = int(getUserPoint(username))
        if userscore == '-1' :
            userscore = 0
            updateUserPoints(True,username,userscore)
        while userChoice != -1 :
            score_du_question = genererDesQuestion()
            userscore = userscore + score_du_question
            print('Vous Voullez Continuer Le Jeu')
            print('-1 : Quitter')
            userChoice = int(input("----> "))     
        updateUserPoints(False, username, userscore)  
        print('################################### Au Revoir ###################################')    
    except :
        print('Erreur Au niveau du programme')
########################################################################################################################