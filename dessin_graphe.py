import networkx as nx
import matplotlib.pyplot as plt

# Matrice d'adjacence du graphe orienté pondéré
matrice = [[0, 1, 3, 0],
           [0, 0, 2, 4],
           [0, 0, 0, 5],
           [0, 0, 0, 0]]

# Création du graphe orienté pondéré à partir de la matrice d'adjacence
G = nx.DiGraph() #Permet d'avoir un graphe orienté
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        if matrice[i][j] > 0:
            G.add_edge(i, j, weight=matrice[i][j]) #ajoute l'arrete au graphe G si son poids > 0

# Dessin du graphe orienté pondéré
pos = nx.spring_layout(G) #détermine la position de chaque noeud dans le graphe
nx.draw(G, pos, with_labels=True) #dessine le graphe G avec les coordonnées de pos

# Dessin des poids des arcs
labels = nx.get_edge_attributes(G, "weight") #Récupere les poids des arretes
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) #Ajoute les labels sur le graphe

# Affichage du graphe dessiné
plt.show()