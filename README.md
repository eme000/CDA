# mise en route


deploiment du serveur web sur un rasberry pi 4 argon M.2 sata

faire le deploiment du pi avec le boot sur le port usb avec le ssd sata m.2 via ce lien :https://github.com/eme000/raspi/blob/main/Installation%20pour%20Raspberry%20Pi%20avec%20Boot%20sur%20USB.md

deployer en premier docker via ce lien:
https://github.com/eme000/CDA/blob/main/Procedure/DockerInstall.md



## cloner le projet github:

cloner ce github : https://github.com/eme000/CDA

installer tout ce qui se trouve dans le fichier requirements.txt a la racine du projet github

avec cette commande : 'trouver la commande'


## nous allons maintent deplpoyer 4 conteneur differents :


# 1 et 2 adminer/ my sql 

sur ce lien

http://localhost:9000/#!/1/docker/stacks

en haut a droite clikcer sur "add stack "

les deux permiers conteneurs vous etre deployer sous un stack : https://github.com/eme000/CDA/blob/main/Procedure/stack_bdd_.md.



#3 image my node red 

dans les conteneur maintenant ajouter my node red

http://localhost:9000/#!/1/docker/containers

https://hub.docker.com/search?q=mynodered

#4 image du serveur web


je sais pas encore




