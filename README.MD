Fanoron-telo - Projet IA

---

## 1. En-tête institutionnel

Site officiel de l'ISPM : www.ispm-edu.com
Nom du groupe de projet : MIABO

---

## 2. Description du travail réalisé

Le projet consiste à développer une version numérique du jeu Fanoron-telo.

L’application permet :

- de jouer contre un autre joueur humain
- de jouer contre une intelligence artificielle
- de visualiser le plateau de jeu
- de respecter toutes les règles du jeu traditionnel

Deux IA ont été implémentées :

- une IA facile (aléatoire)
- une IA difficile basée sur Minimax + Alpha-Beta

---

## 3. Guide d’installation RAPIDE

Prérequis

- Python 3.x installé
- VS Code (optionnel)

Installation

```bash
git clone https://github.com/Aina4296/AlgoAvance.git
cd fanoron-telo
python main.py
```

---

## 4.Outils d'aide d'IA utilisé

Nous avons utilisé Claude et ChatGPT pendant le développement du projet. On avait besoin d'assistant intelligent pour accélerer le projet, CLaude était important pour le débogage mais en gain de temps, c'es l'avantage du CHATGPT

---

## 5- Modélisation et algorithme de l'IA DU JEU

Dans ce jeu Fanoron-telo, on a fait une intelligence artificielle pour jouer contre le joueur

Le plateau du jeu est fait avec une liste de 9 cases.

Chaque case peut être :

- vide ""
- ou contenir un joueur "X" ou "O"

Donc on a quelque chose comme :
[ "", "", "", "", "", "", "", "", "" ]
L’IA facile est très simple.

Elle ne réfléchit pas beaucoup.

Elle fait juste :

- elle regarde les cases vides
- elle choisit une case au hasard

Donc elle peut perdre facilement.

L’IA difficile est plus intelligente.

Elle utilise un algorithme qui s’appelle Minimax.

Cet algorithme :

- essaye tous les coups possibles
- regarde si le joueur peut gagner
- choisit le meilleur coup pour gagner ou bloquer

On a aussi ajouté Alpha-Beta.

Ça sert à :

- ne pas calculer des coups inutiles
- rendre l’IA plus rapide

Résumé simple

- IA facile = joue au hasard
- IA difficile = réfléchit beaucoup avec Minimax
- Alpha-Beta = aide pour aller plus vite

Conclusion

Avec cette IA, le jeu peut jouer contre un humain et essayer de gagner ou bloquer les coups.

---

##6-Analyses de performance
