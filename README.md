# mise en route


deploiment du serveur web sur un rasberry pi 4 argon M.2 sata

faire le deploiment du pi avec le boot sur le port usb avec le ssd sata m.2 via ce lien :https://github.com/eme000/raspi/blob/main/Installation%20pour%20Raspberry%20Pi%20avec%20Boot%20sur%20USB.md

deployer en premier docker via ce lien:
https://github.com/eme000/CDA/blob/main/Procedure/DockerInstall.md



# Cloner le projet github:

cloner ce github : https://github.com/eme000/CDA

```
git clone https://github.com/eme000/CDA
```


installer tout ce qui se trouve dans le fichier requirements.txt a la racine du projet github

```
cd CDA/02_Client_leger/WEB_FLASK/

pip install -r requirements
```

si l'installation de my sql connector ne fonction pas il faut passer par un environement virtuel et reinstaller  :https://github.com/eme000/raspi/blob/main/mysql_connector.md




# nous allons maintent deplpoyer 4 conteneur differents :


## 1 et 2 adminer/ my sql 

sur ce lien

http://localhost:9000/#!/1/docker/stacks

en haut a droite clikcer sur "add stack "


les deux permiers conteneurs vous etre deployer sous un stack  attention modifier le mdp root : https://github.com/eme000/CDA/blob/main/Procedure/stack_bdd_.md.

importer une des deux bdd dans le git avec/sans données 

les deux export sql se trouve ici:

https://github.com/eme000/CDA/blob/main/01_BDD/

## 3 image my node red 

dans les conteneur maintenant ajouter my node red

crée un nouveau conteneur via cmd

dans le lien de l'image mettre 
```
docker run -it -p 1880:1880 -v myNodeREDdata:/data --name mynodered nodered/node-red
```
https://hub.docker.com/r/nodered/node-red


## 4 image du serveur web


je sais pas encore


## 5 lancement serveur web 

assurez vous de renter les bonnes données de connection a la bdd dans  .env 
``` 02_Client_leger/WEB_FLASK/app/.env ```

lancement dans un environement virtuel :

```
source myenv/bin/activate
/CDA/02_Client_leger/WEB_FLASK/
python serverWEB.py
```

#lancer les conteneur et aller sur l'addresse du pi, port 5000



