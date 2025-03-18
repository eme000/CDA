# Mise en route

## Déploiement du serveur web sur un Raspberry Pi 4 Argon M.2 SATA

Effectuer le déploiement du Raspberry Pi avec le boot sur le port USB en utilisant un SSD SATA M.2 via ce [lien](https://github.com/eme000/raspi/blob/main/Installation%20pour%20Raspberry%20Pi%20avec%20Boot%20sur%20USB.md).

## Ventilateur du boîtier Argon à 100%

```
curl https://download.argon40.com/argon1.sh | bash

argonone-config
```

Configuration :

- 1
- Y
- 1
- 0

## Déployer Docker en premier via ce lien :

[Installation de Docker](https://github.com/eme000/CDA/blob/main/Procedure/DockerInstall.md)

## Cloner le projet GitHub

Cloner le dépôt GitHub suivant :

```
git clone https://github.com/eme000/CDA
```

Installer toutes les dépendances listées dans le fichier `requirements.txt` à la racine du projet GitHub.

Si l'installation de MySQL Connector ne fonctionne pas, il faut passer par un environnement virtuel et le réinstaller : [MySQL Connector](https://github.com/eme000/raspi/blob/main/mysql_connector.md).

```
cd CDA/02_Client_leger/WEB_FLASK/

pip install -r requirements.txt
```

Modifier le login/mot de passe de la base de données dans le fichier `.env` qui se trouve ici :

```
cd CDA/02_Client_leger/WEB_FLASK/app/
nano .env
```

## Déploiement de 4 conteneurs différents

### 1 et 2 : Adminer / MySQL

Accédez au lien suivant :

[Stacks](http://localhost:9000/#!/2/docker/stacks)

En haut à droite, cliquez sur "Add Stack".

Les deux premiers conteneurs doivent être déployés sous une stack. Attention, modifiez le mot de passe root : [Instructions Stack BDD](https://github.com/eme000/CDA/blob/main/Procedure/stack_bdd_.md).

Créer une base de données via cette requête sur Adminer :

[Adminer](http://0.0.0.0:8080/?server=db&username=root&sql=)

```
CREATE DATABASE IF NOT EXISTS bdd_production CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

[Importer une des deux bases de données sur Adminer](http://0.0.0.0:8080/?server=db&username=root&db=bdd_production&sql=)

Importer les données via le bouton "Requête SQL".

Les fichiers d'export SQL se trouvent ici :

- [Export BDD sans données](https://github.com/eme000/CDA/blob/main/01_BDD/export_bdd_sans_donnees.txt)
- [Export BDD avec données](https://github.com/eme000/CDA/blob/main/01_BDD/export_bdd_avec_donnees.txt)

### 3 : Image My Node-RED

Ajouter le conteneur My Node-RED.

Créer un nouveau conteneur via la commande suivante :

```
docker run -it -p 1880:1880 -v myNodeREDdata:/data --name mynodered nodered/node-red
```

[Docker Hub - Node-RED](https://hub.docker.com/r/nodered/node-red)

Importer les fichiers `.json` qui se trouvent dans :

```
CDA/04_node_red/flow.json
```

### 4 : Image du serveur web

Assurez-vous d'entrer les bonnes informations de connexion à la base de données dans le fichier `.env` (notamment pour le mot de passe) :

```
cd CDA/02_Client_leger/WEB_FLASK/app
nano .env
```

Lancer la création du serveur web en Docker depuis l'environnement virtuel :

```
cd CDA/02_Client_leger/WEB_FLASK/
source myenv/bin/activate

docker image build -t flask_docker .
docker run -p 5000:5000 -d flask_docker
```

## Vérification

- [Liste des conteneurs](http://localhost:9000/#!/2/docker/containers)
- [Site Web](http://0.0.0.0:5000/)

