## Install Docker

```
 sudo apt-get remove docker docker-engine docker.io containerd runc

 

sudo apt-get update
 
 sudo apt-get install ca-certificates curl gnupg lsb-release
 
 curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
 
 echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
 
 sudo apt-get update
 
 sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
 
 sudo docker --version

 
 mkdir ~/Documents/DOCKER &&  cd ~/Documents/DOCKER

```
- `sudo docker run hello-world`
- `sudo docker images` Vérifier qu'une image container hello-world existe
- `sudo docker ps -a` Vérifier que le container s'execute bien
- `sudo docker compose version` Vérifier installation et version de docker compose, si V2+ alors syntaxe `docker compose up -d` au lieu de `docker-compose up -d`en V1

[DockerInstall](https://docs.docker.com/engine/install/debian/)

## Run Docker commands without sudo

- ```sudo groupadd docker```
- ```sudo gpasswd -a $USER docker```
- **LOGOUT fom Linux session to force group membership re-evaluation**
- ```sudo service docker restart```

## Install Portainer

![Portainer](./PORTAINER.png "PORTAINER")

[PortainerAdmin](http://192.168.0.17:9000)

- ```docker volume create portainer_data```
- ```docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer:latest```
- ```firefox localhost:9000 &``` accès à la page de configuration de Portainer
  - username => admin 
  - password => portainer (the password must be at least 8 characters long) v2.0
  - password => portainer3556 (the password must be at least 12 characters long) v2.16
  - Create user
  - selectionner l'emplacement Local dans Environnement

## Docker multi instance

[DockerScale](https://pspdfkit.com/blog/2018/how-to-use-docker-compose-to-run-multiple-instances-of-a-service-in-development/)

## docker non-overlapping ipv4 address pool among the defaults to assign to the network

- `docker network ls`
- `docker network prune`
- `docker network ls`

## Clean Up Docker overlay

- `df -h` check the memory used, to be sure, memory is used by overlay folder
- `docker system df` to check what is using space
- `docker system prune -a -f` cleans up also networks, build cache, etc
- `docker container prune`
- `docker image prune -a`
- `systemctl stop docker`
- `rm -rf /var/lib/docker/overlay/*`
- `for d in $(find /var/lib/docker/image/overlay -type d -name '*sha256*'); do echo rm -rf $d/* ; done`
- `sudo reboot now`
- `df -h` to be sure, overlay data is removed 

[CleanOverlay](https://stackoverflow.com/questions/31712266/how-to-clean-up-docker-overlay-directory)

[DockerGarbageCollector](https://github.com/spotify/docker-gc)

[cronDocker](https://github.com/flaccid/docker-docker-gc-crond)
