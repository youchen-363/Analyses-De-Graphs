import numpy as np
import matplotlib.pyplot as plt
import time

##############################################################################
### Fonction de génération d'un parcours en Largeur à partir d'une matrice ###
##############################################################################

def parcoursLargeur(matrice,sommet):
    taille  = len(matrice)
    couleur = {}
    
    # On colorie tous les sommets en blanc
    for i  in range(taille):
        couleur[i] = 'blanc'
    
    # Initialisation des variables en coloriant le sommet de départ en vert, la file à sommet et le resultat à sommet
    couleur[sommet] = 'vert'
    file = [sommet]
    Resultat = [sommet]
    
    while file != []:
        # on prend le premier terme de la file
        i = file[0]
        for j in range(taille):
            # On enfile les successeurs de i encore blancs:
            if (matrice[file[0]][j] == 1 and couleur[j] == 'blanc'):
                file.append(j)
                # On les colorie en vert (sommets visités)
                couleur[j] = 'vert'
                # On les place dans la liste Resultat
                Resultat.append(j) 
                
        # on défile i (on retire le premier élément)
        file.pop(0)
    
    return Resultat


#################################################################################
### Fonction de génération d'un parcours en profondeur à partir d'une matrice ###
#################################################################################

def parcoursProfondeur(matrice,sommet):
    # taille du tableau = nombre de sommets
    taille=len(matrice)
    couleur={}     # On colorie tous les sommets en blanc et s en vert

    # On colorie tous les sommets en blanc
    for i  in range(taille):
        couleur[i] ='blanc'

    # Initialisation des variables en coloriant le sommet de départ en vert, la pile à sommet et le resultat à sommet
    couleur[sommet] ='vert'
    pile = [sommet]
    Resultat = [sommet]
    
    while pile !=[]:
        # on prend le dernier sommet i de la pile
        i=pile[-1]
        # on crée la liste de ses successeurs non déjà visités (blancs)
        Succ_blanc=[]

        # Ajout d'un successeur 
        for j in range(taille):
            if (matrice[i,j] == 1 and couleur[j]=='blanc'):
                Succ_blanc.append(j)
        # Verification de la présence d'un successeur
        if Succ_blanc!=[]:
            # Selection du premier successeur
            valeur= Succ_blanc[0]
            # Colorisation du successeur en vert
            couleur[valeur]='vert'
            # Empilement du successeur
            pile.append(valeur)
            # Ajout dans la liste de résultat
            Resultat.append(valeur)
        else:
            # on sort le sommet courant de la pile
            pile.pop()          
    
    return Resultat


###########################################################
### Fonction de vérification de la connexité d'un graph ###
###########################################################

def isMatriceConnexe(matrice):
    # Initialisation de la taille de la matrice à comparer avec la taille des parcours
    taille = len(matrice)
    
    # Visualisation de tous les parcours
    for i in range (taille):
        compare = len(parcoursProfondeur(matrice, i))
        if compare == taille:
            return True
        
    return False

############################################################################
### Fonction de génération d'un parcours linéaire à partir d'une matrice ###
############################################################################

def parcoursLineaire(matrice):
    # Initialisation d'une liste de sommets vide
    liste = []

    # Ajout des sommets dans l'ordre alphabetique
    for i in range (len(matrice)):
        liste.append(i)
    
    # Renvoi de la liste du parcours linéaire
    return liste


################################################################################################
### Fonction de génération d'une matrice d'incidence à partir d'une matrice de graph pondéré ###
################################################################################################

def incidence(matrice):

    # Initialisation des variables taille étant la taille de la matrice en parametre et incidence une copie de la matrice en parametre
    taille = len(matrice)
    incidence = np.copy(matrice)
    
    # Boucle de remplacement des valeurs infini par 0 et des autres valeurs par 1
    for i in range (taille):
        for j in range (taille):
            if incidence[i][j] == float('inf'):
                # Remplacement des infini par 0
                incidence[i][j] = 0
            else:
                # Remplacement des autres valeurs par 1
                incidence[i][j] = 1
    
    # Renvoi de la matrice d'incidence
    return incidence


###################################################################################################
### Fonction de génération d'une matrice d'incidence à partir d'une taille et d'une probabilité ###
###################################################################################################

def matrice_prob(n,p):
    # Générer une matrice incidence taille n avec probabilité de 1, p
    matrix_incidence = np.random.binomial(1, p, (n, n))
    return matrix_incidence 


#####################################################################
### Fonction de génération d'un graph pondéré avec 50% de flèches ###
#####################################################################

def graphe(taille, borneInf, borneSup):
    # Génération d'une matrice carrée de dimension "taille" ayant une proportion de 1 et de 0 de 50%
    matrice = np.random.randint(0,2, (taille,taille))

    # Conversion de la matrice en coefficients de type float
    matrice=matrice.astype('float64')

    # Parcours de la matrice et conversion des valeurs de la matrice : les 1 en valeur aléatoire et les 0 en infini
    for i in  range(taille):
        for j in range(taille):
            if matrice[i][j] == 1:
                # remplacement des 1 par des valeures comprises entre borneInf incluse et borneSup excluse
                matrice [i][j] = np.random.randint(borneInf, borneSup)
            else:
                # Remplacement des 0 par infini
                matrice [i][j] = float('inf')

    # Renvoi de la matrice
    return matrice


##################################################################################
### Fonction de génération d'un graph avec une proportion variables de flèches ###
##################################################################################

def graphe2(taille, proportion, borneInf, borneSup):
    # Génération d'une matrice carrée de dimension "taille" ayant une proportion de 1 de "proportion" et le reste de 0
    matrice = np.random.binomial(1, proportion, (taille, taille))

    # Conversion de la matrice en coefficients de type float
    matrice=matrice.astype('float64')

    # Parcours de la matrice et conversion des valeurs de la matrice : les 1 en valeur aléatoire et les 0 en infini
    for i in  range(taille):
        for j in range(taille):
            if matrice[i][j] == 1:
                # remplacement des 1 par des valeures comprises entre borneInf incluse et borneSup excluse
                matrice [i][j] = np.random.randint(borneInf, borneSup)
            else:
                # Remplacement des 0 par infini
                matrice [i][j] = float('inf')

    # Renvoi de la matrice
    return matrice


##############################################################################
### Fonction de calcul du plus court chemin avec l'algorithme de dijkistra ###
##############################################################################

def Dijkstra(M, d):
    # Initialisation
    n = len(M)
    # initialisation du dictionnaire dist avec tous les sommets à l'infini
    dist = {s: float('inf') for s in range(n)}
    # initialisation du dictionnaire prédecesseur
    pred = {s: None for s in range(n)}
    # initialiser la distance du sommet de départ à 0
    dist[d] = 0
    # un ensemble pour les sommets non choisis
    distR = {s for s in range(n)}

    # Tant qu'il reste un sommet à traiter
    while distR:
        # Initialisation des variables de recherche de sommet ayant une distance minimale
        dist_min = float('inf')
        sommet_min = None
        # Chercher le sommet avec la distance minimale
        for v in distR:
            # Vérifie si la distance de v est inférieure à la distance minimale actuelle
            if dist[v] < dist_min:
                # Met à jour la distance minimale avec la distance de v
                dist_min = dist[v]
                # Met à jour le sommet avec le sommet v ayant la distance minimale
                sommet_min = v

        if sommet_min is not None:
            # Supprimer le sommet avec la distance minimale de distR
            distR.remove(sommet_min)
        else:
            break

        # Parcourir tous les sommets adjacents à sommet_min
        for t in range(n):
            if M[sommet_min][t] > 0:
                # Mettre à jour la distance des sommets s'il existe un chemin plus court
                if dist[sommet_min] + M[sommet_min][t] < dist[t]:
                    dist[t] = dist[sommet_min] + M[sommet_min][t]
                    pred[t] = sommet_min

    results = {}
    for s in range(n):
        if dist[s] == float('inf'):
            # Le sommet n'est pas joignable à d par un chemin dans le graphe G
            results[s] = [float('inf'), "sommet non joignable à d par un chemin dans le graphe G"]
        else:
            # Affectation du chemin le plus court
            chemin = [s]
            # Initialiser p avec s, le dernier sommet du chemin le plus court
            p = s

            # Remonter le chemin à partir du prédecesseur jusqu'à d
            while pred[p] is not None:
                chemin.insert(0, pred[p])
                p = pred[p]
            
            # Ajout au tableau de résultats la distance du chemin le plus court pour le sommet en cours et son parcours
            results[s] = [dist[s], chemin]
    
    return results



################################################################################
### Fonction de calcul du plus court chemin avec l'algorithme de BellmanFord ###
################################################################################

def BellmanFord(matrice, Sommet, ParcoursType):
    # initialisation des variables de calcul : matrice d'incidence, liste des sommets ordonnée
    taille = len(matrice)
    matriceIncidence = incidence(matrice)
    
    # Choix de la liste de sommets
    if ParcoursType == "LARGEUR":
        listeSommets = parcoursLargeur(matriceIncidence, Sommet)
    elif ParcoursType == "PROFONDEUR":
        listeSommets = parcoursProfondeur(matriceIncidence, Sommet)
    elif ParcoursType == "LINEAIRE":
        listeSommets = parcoursLineaire(matriceIncidence)
    else:
        return "Type de parcours invalide", "Type de parcours invalide"

    # Ajout des sommets n'apparaissant pas dans la liste
    for i in range(taille):
        if i not in listeSommets:
            listeSommets.append(i)
            
    
    # Création de la liste des flèches ordonnées
    listeFleches = []
    for i in listeSommets:
        for j in range(taille):
            # Ajout d'une fleche dans la liste de fleche si elle existe dans la matrice
            if matriceIncidence[i][j] == 1:
                tupleAAjouter = (i,j, matrice[i][j])
                listeFleches.append(tupleAAjouter)
                
    # Initialisation des dictionnaires de données de poids et de prédécesseurs
    poidSommet = {}
    predSommet = {}
    for i in listeSommets:
        # Initialisation du sommet de départ à distance = 0 et predecesseur = lui-meme
        if i == Sommet:
            poidSommet[i] = 0
            predSommet[i] = i
        # Initialisation des autres sommets à distance = infini et pas de predessesseur
        else:
            poidSommet[i] = float('inf')
            predSommet[i] = None
        
    # Initialisation des variables de vérification du nombre de tour et d'actualisation 
    iteration = 0
    actualisation = True
    
    # Boucle d'actualisation des predecesseurs et des poids (distances)
    while iteration < taille and actualisation == True:
        actualisation = False
        
        # Parcours de la liste de fleches
        for fleche in listeFleches:
            
            # Modification des predecesseurs et des poids
            if fleche[2] + poidSommet[fleche[0]] < poidSommet[fleche[1]]:
                poidSommet[fleche[1]] = fleche[2] + poidSommet[fleche[0]]
                predSommet[fleche[1]] = fleche[0]
                #Actualisation effectuée
                actualisation = True
        
        # Actualisation du nombre d'itérations
        iteration +=1

    # Déclaration de la variable de type tableau stockant le résultat
    tableauDeResultat = []
    
    # Vérification et renvoie du résultat adéquat
    if iteration == taille:
        return "Sommets joignables mais présence d’un cycle de poids négatif", iteration
    else:
        # Attribution du résultat pour chaque sommet autre que le sommet de départ
        for sommetTest, distance in poidSommet.items():
            if sommetTest != Sommet:
                # Attribution du résultat : sommet non joignable pour les sommets n'ayant pas de suite de predecesseurs menant au sommet de départ
                if distance == float('inf'):
                    tupleToAdd = f"Le sommet {sommetTest} n'est pas joignable à {Sommet}"
                else:
                    # Définition de la suite de sommets parcourus du sommet de départ au sommet en cours et du poids total du chemin
                    itineraire = []
                    itineraire.append(sommetTest)
                    predessesseur = sommetTest
                    # Création du parcours effectué en ajoutant dans l'ordre les predecesseurs des predecesseurs jusqu'au sommet de départ
                    while predessesseur != Sommet:
                        predessesseur = predSommet[predessesseur]
                        itineraire.append(predessesseur)
                    # Création de la ligne de résultat correspondant au sommet en cours en affichant la distance au sommet et le parcours créé inversé (du sommet de départ au sommet en cours)
                    tupleToAdd = (f"Chemin le plus court du sommet {Sommet} pour aller à {sommetTest} : {poidSommet[sommetTest]}", f"itinéraire du sommet {Sommet} au sommet {sommetTest} : {itineraire[::-1]}")
                
                # Ajout du résultat dans le tableau de résultats
                tableauDeResultat.append(tupleToAdd)
        
        # Renvoie du tableau de résultat et du nombre de cycles effectués avant d'y parvenir
        return tableauDeResultat, iteration


#############################################################################################################
### Fonction de calcul du temps d'execution de l'algorithme de Dikistra pour une martice de taille donnée ###
#############################################################################################################

def TempsDij (taille, affichage, proportion) :
    # Génération de la matrice pondérée de taille "taille" connexe
    matrice = graphe2(taille,proportion,0,100)

    # Décompte de la durée d'execution
    start = time.perf_counter()
    Dijkstra(matrice, 0)
    duree = time.perf_counter() - start

    # Affichage de la durée d'execution
    if affichage:
        print(f"Le temps d'execution avec dijkistra pour une matrice de taille {taille} est : {duree} secondes")        

    # retourne la valeur de la durée d'execution
    return duree 


################################################################################################################
### Fonction de calcul du temps d'execution de l'algorithme de BellmanFord pour une martice de taille donnée ###
################################################################################################################

def TempsBF(taille, affichage, proportion):
    # Génération de la matrice pondérée de taille "taille" et de proportion de flèches "proportion"
    matrice = graphe2(taille,proportion,0,100)

    # Déclaration de la constante de type de parcours
    LARGEUR = "LARGEUR"

    # Décompte de la durée d'execution
    start = time.perf_counter()
    BellmanFord(matrice, 0, LARGEUR)
    duree = time.perf_counter() - start

    
    # Affichage de la durée d'execution
    if affichage:
        print(f"Le temps d'execution avec BellmanFord pour une matrice de taille {taille} est : {duree} secondes")

    # retourne la valeur de la durée d'execution
    return duree       



################################################################################################################
### Fonction de test des nombres de cycles pour l'algorithme de BellmanFord  ###
################################################################################################################

def TestsBellmanFordParcours(matrice, sommet):
    # Initialisation des constantes
    PROFONDEUR = "PROFONDEUR"
    LARGEUR = "LARGEUR"
    LINEAIRE = "LINEAIRE"

    # Attribution des valeurs
    graph, cycleProfondeur = BellmanFord(matrice,sommet, PROFONDEUR)
    graph, cycleLargeur = BellmanFord(matrice,sommet, LARGEUR)
    graph, cycleLienaire = BellmanFord(matrice,sommet, LINEAIRE)

    # Affichages
    print(f"Nombre de cycle avec parcours lineaire : {cycleLienaire}")
    print(f"Nombre de cycle avec parcours en profondeur : {cycleProfondeur}")
    print(f"Nombre de cycle avec parcours en largeur : {cycleLargeur}")


#####################################################################################################
### Fonction d'affichage du temps déexecution de djikistra en fonction de la taille de la matrice ###
#####################################################################################################

def complexiteDijkistra(affichage):

    # Initialisation de la liste de durée et de tailles
    list_time = []
    taille = []

    # Enregistrement des durées d'execution
    for i in range (2,200):
        if affichage:
            list_time.append(TempsDij(i, affichage, 0.5))
        else:
            list_time.append(TempsDij(i, False, 0.5))
        taille.append(i)

    # Affichage du graphique
    plt.plot(taille,list_time)
    plt.title("Complexité de Dijkistra en fonction de la taille de la matrice")
    plt.show()


#######################################################################################################
### Fonction d'affichage du temps déexecution de BellmanFord en fonction de la taille de la matrice ###
#######################################################################################################

def complexiteBellmanFord(affichage):

    # Initialisation de la liste de durée et de tailles
    list_time = []
    taille = []

    # Enregistrement des durées d'execution
    for i in range (20,200):
        if affichage:
            list_time.append(TempsBF(i, affichage))
        else:
            list_time.append(TempsBF(i, False))
        taille.append(i)

    # Affichage du graphique
    plt.plot(taille,list_time)
    plt.title("Complexité de BellmanFord en fonction de la taille de la matrice")
    plt.show()

    
####################################################################################################################
### Fonction d'affichage comparatif des temps d'éxecution des algorithmes en fonction de la taille de la matrice ###
####################################################################################################################

def comparaisonComplexite():
        # Initialisation de la liste de durée et de tailles
    list_Dij_time = []
    list_BF_time = []
    taille = []

    # Enregistrement des durées d'execution
    for i in range (2,200):
        list_Dij_time.append(TempsDij(i, False, 1/i))
        list_BF_time.append(TempsBF(i, False, 1/i))
        taille.append(i)

    # Affichage du graphique classique
    plt.plot(taille,list_Dij_time, label="Dijkstra")
    plt.plot(taille,list_BF_time, label="BellmanFord")
    plt.title("Comparaison des complexités en fonction de la taille des matrices")
    plt.legend()
    plt.show()
    
    # Affichage du graphique en log log
    plt.plot(taille,list_Dij_time, label="Dijkstra")
    plt.plot(taille,list_BF_time, label="BellmanFord")
    plt.title("Comparaison des complexités en fonction de la taille des matrices (log log)")
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


#########################################################################################################
### Fonction d'affichage de test de la forte connexité d'une matrice à partir d'une matrice incidence ###
#########################################################################################################

def fc(M) :
    # Attribution à la variable taille la dimension de la matrice pour le parcours matriciel
    taille = len(M)
    
    # Création d'une matrice de fermeture Transitive
    fermetureT = M
    
    # Parcours de la matrice
    for i in range(taille) :
        for j in range(taille) :
            # Detection des flèches dans la matrice
            if (M[j,i] ==1) :
                for k in range(taille) :
                    # Création d'une fleche entre 2 sommets s'il existe un sommet intermediaire permettant d'aller d'un sommet à l'autre
                    if (M[i,k]==1):
                        fermetureT[j,k] = 1
    
    # Création de la matrice de 1 de dimension de la matrice d'origine
    matriceUn = np.ones_like(M)
    
    # Retourner le resultat de la comparaison des matrice
    return np.array_equal(matriceUn, fermetureT)


#############################################################################################
### Fonction retournant le pourcentage de graphes pondérés de taille n fortement connexes ###
#############################################################################################

def test_stat_fc(n):
    # Nombre de tests à effectuer
    num_tests = 200
    # compteur des graphes fortement connexes 
    compteur = 0 
    
    # Faire une boucle avec le nombre de tests 
    for _ in range(num_tests):
        # Générer une matrice aléatoire de taille n avec p, probabilité de 1
        matrix = matrice_prob(n,0.5)
        # Vérifier si le graphe est fortement connexe
        if fc(matrix) :
            compteur += 1
    
    # Calculer le pourcentage de graphes fortement connexes
    pourcentage_connexite_fort = (compteur / num_tests) * 100  
    
    # renvoyer la pourcentage de graphes fortement connexes
    return pourcentage_connexite_fort

def test_stat_fc2(n,p):
    # Nombre de tests à effectuer
    num_tests = 200
    # compteur des graphes fortement connexes 
    compteur = 0 
    
    # Faire une boucle avec le nombre de tests 
    for _ in range(num_tests):
        # Générer une matrice aléatoire de taille n avec p, probabilité de 1
        matrix = matrice_prob(n,p)
        # Vérifier si le graphe est fortement connexe
        if fc(matrix) :
            compteur += 1
    
    # Calculer le pourcentage de graphes fortement connexes
    pourcentage_connexite_fort = (compteur / num_tests) * 100  
    
    # renvoyer la pourcentage de graphes fortement connexes
    return pourcentage_connexite_fort



#####################################################################################
### Fonction déterminant le seuil de forte connexité pour une matrice de taille n ###
#####################################################################################

def seuil(n) : 
    # probabilité de 1 dans la matrice 
    p = 0.5
    # pourcentage des matrices fortement connexes
    c = 100
    # tant que les matrices sont fortement connexes
    while c>99 : 
        # obtenir le pourcetage des matrices fortement connexes 
        c = test_stat_fc2 (n,p)
        #diminuer la probabilité de 1 
        p -= 0.01
    return p


###########################################################################################################
### Fonction d'affichage de la représentation graphique du seuil en fonction de la taille de la matrice ###
###########################################################################################################

def representationSeuil():
    # Représentation graphique de seuil(n)
    x = []
    y = []
    
    # Enregistrement des valeurs dans les listes
    for i in range(10,41) :
        x.append(i)
        y.append(seuil(i))

    # Création et affichage du graphique
    plt.plot(x,y)
    plt.xlabel('Taille de matrice')
    plt.ylabel('Seuil')
    plt.title('Variation du seuil en fonction de n')
    plt.show()

    
##############################################################################################################
### Fonction d'affichage de la représentation graphique du pourcentage de graphes connexe à 50% de flèches ###
##############################################################################################################

def graphSeuil50prct():
    
    # Liste stockant les pourcentages de
    liste_prct = []
    liste_taille = []
    
    # Enregistrement des valeurs dans les listes
    for i in range(2,50):
        print(f"matrice de taille {i} en cours")
        liste_prct.append(test_stat_fc2(i,0.5))
        liste_taille.append(i)
    
    # Création et affichage du graphique
    plt.plot(liste_taille,liste_prct)
    plt.xlabel('Taille de matrice')
    plt.ylabel('porcentage de matrices connexes')
    plt.title('Variation du pourcentage de connexité en fonction de la taille de la matrice')
    plt.show()
    
    
#####################
### question 10.2 ###
#####################

### same solutions to question 6.2

x = []
y = []
for n in range(10,41) :
    x.append(n)
    y.append(seuil(n))
    print(n,':', True)
    
# fonction covariance of numpy ne fonction pas avec array I've created a function
def cov(x,y) :
    n = 31
    meanX = np.mean(x)
    meanY = np.mean(y)
    for i in range (n) :
        p = (x[i]-meanX)*(y[i]-meanY)
    return p/n

# same for variance
def var(x) :
    n = 31
    meanX = np.mean(x)
    for i in range (n) :
        p = (x[i]-meanX)**2
    return p/n

logx = np.log(x)
logy = np.log(y)
covXY = cov(logx, logy)
varX = var(logx)
a = covXY / varX # la pente de la droite
logc = np.mean(logy) - a*np.mean(logx)
c = np.exp(logc)

# avec la pente a, on peut trouver ~ -0.707 
# c j'ai trouvé ~ 2.8567 mais ce n'est pas important
# car dans le fonction seuil, c est la probabilité de 1 dans la matrice
# qui ne peut pas dépasser 1 (le plus grand valeur de la probabilité 
# mais avec la calculation il n'y a pas ce limite donc on peut trouver un grand valeur 
# mais c on s'en fiche, ce qu'ils attendent est le a (coefficient directeur de la droite) 
    
    
    