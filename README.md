# Scanner de réseau en Python

## 1. Présentation du projet

Ce projet consiste à développer un outil simple de scan réseau en Python permettant de vérifier la disponibilité des adresses IP d'un réseau donné à l'aide de la commande `ping`.

L'utilisateur saisit une adresse réseau au format CIDR. Le programme vérifie sa validité, parcourt les adresses IP utilisables et effectue un test de connectivité sur chacune d'elles.

## 2. Objectifs du projet

- Comprendre le fonctionnement du scan réseau.
- Manipuler les adresses IP et les réseaux en Python.
- Automatiser l'exécution de commandes système.
- Vérifier la connectivité entre des machines.
- Se familiariser avec les modules Python dédiés aux réseaux.

## 3. Technologies utilisées

- **Python 3** : langage de programmation.
- **ipaddress** : validation et manipulation des adresses IP.
- **subprocess** : exécution des commandes système.
- **platform** : identification du système d'exploitation.

## 4. Fonctionnalités

- Saisie d'une adresse réseau.
- Validation de l'adresse réseau au format CIDR.
- Identification des adresses IP utilisables.
- Exécution automatique de la commande `ping`.
- Compatibilité avec Windows et Linux.

## 5. Structure du projet

```text
scanner-reseau/
│
├── main.py
├── README.md
└── .gitignore
```

## 6. Prérequis

Avant d'exécuter le programme, il faut disposer de :

- Python 3 installé.
- Une connexion réseau.
- La commande `ping` disponible sur le système.

Aucune bibliothèque externe supplémentaire n'est nécessaire.

## 7. Installation et exécution

### Étape 1 : Récupérer le projet

Télécharger ou cloner le dépôt GitHub.

### Étape 2 : Accéder au dossier

```bash
cd scanner-reseau
```

### Étape 3 : Exécuter le programme

```bash
python3 main.py
```

### Étape 4 : Saisir le réseau à scanner

Exemple :

```text
Veuillez entrer le réseau à scanner : 192.168.1.0/24
```

Le programme parcourt les adresses IP utilisables et effectue un test de connectivité avec `ping`.

## 8. Fonctionnement technique

Le programme utilise quatre éléments principaux :

- `ipaddress.ip_network()` : vérifie et représente le réseau saisi.
- `reseau.hosts()` : récupère les adresses IP utilisables du réseau.
- `subprocess.run()` : exécute la commande ping.
- `platform.system()` : adapte le paramètre de ping au système d'exploitation.

## 9. Limites actuelles

- Le programme ne distingue pas encore explicitement les adresses IP accessibles et inaccessibles dans son affichage.
- Le temps d'attente des commandes ping n'est pas encore configuré.
- Le scan porte sur les adresses IP utilisables du réseau saisi.

## 10. Évolutions envisagées

- Identifier clairement les machines accessibles et inaccessibles.
- Afficher un résumé du scan.
- Ajouter la gestion des délais d'attente.
- Améliorer l'affichage des résultats.
- Ajouter une exportation des résultats dans un fichier.

## 11. Auteur

**NOUKOUKOU Sényényo Gianni Loïc**

Étudiant en Systèmes et Réseaux Informatiques.

---

*Projet personnel réalisé dans le cadre de l'apprentissage de Python et de l'automatisation des tâches réseau.*
