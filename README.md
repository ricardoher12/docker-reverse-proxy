# docker-reverse-proxy

A reverse-proxy is configured to redirect to a web app and a python-flask app, each applicattion runs in a different container and communicates each other through the network created by the docker-compose file

##Web App
Nginx was used to host the static web site. 

##Python Flask App
The app connects to redis to store the times that it is visited. 

##Proxy
Ngnix was configured to work as a reverse proxy, the url for the wep app is /app_1 and for the python app is /app_2.

##Docker Compose

This file contains the configuration of the four containers needed to create the apps and the reverse proxy.

* nginx: represents the reverse proxy container,  it is configured to listen on port 8081, also it depends on app_1 abd app_2 contaners.

* app_1: represents the web app container, it is config to on port 80 and also expose that port..

* app_2: represents the python-flask contaner, is configured to listen on port 5000, it depends on the redis container.

* redis: is the redis container to which the phyton app will connect to.

## Project Diagram
<img src="/architecture/architecture.jpg" alt="Project Diagram"/>