1- If Docker containers are like shipping containers, what would the Docker image be?
   Docker image is the template for building the containers as docker uses the instructions present in the dockerfile to build the image,the docker container is an instance of the docker image.

2- You want to ensure your container is running fine and healthy. Which Docker feature will you use to monitor its health?
    "Healthcheck" feature 

3- If a Docker network is like a company's internal LAN, what would docker-compose.yml be?
    Docker would be the network's configuration document,template defining how containers should communicate within the network 

4- You have two services, frontend and backend, and you want to ensure that backend starts before frontend. Which Docker Compose key value will you use?
   The docker compose key value to use is: "depends_on"

5- If Docker volumes are like USB drives, what does the volumes key in Docker Compose do?
   volumes key in Docker compose define where the data should stay between containers restarts

6- You need to create multiple instances of the same service. What feature of Docker Compose will you use?
    "scale" command or defining multiple service instances in the docker compose file.

7- If Docker networks are like chat rooms, what would the bridge network mode be?
   Bridge network mode would be private chat room because it isolates containers from external networks.

8- You want to limit the CPU usage of a specific container. Which Docker Compose key value will you use?
   "cpus" key

9- If the Docker Hub is like a public library, what would docker pull be?
   Docker pull would be like borrowing a book from the shelf to read 

10- You need to pass environment variables to a container to configure its settings. Which Docker Compose key value will you use?
    "environment" key

11- If a Docker container is like a running application on your computer, what would the Dockerfile be?
    Dockerifle would be the instructions for building this application

12-You want to make sure a container only starts if another service is successfully running. Which Docker Compose feature helps with this dependency management?
   depends-on

13- If the Docker Compose file (docker-compose.yml) is like a party invitation list, what would the services section be?
    list of party activities

14- You want to share data between multiple running containers. What Docker feature will you use?
    docker volumes

15- If Docker CLI commands are like the controls on a remote control, what would docker-compose up -d do?
    play button--> starting the containers in detached mode 

16- You need to add a host device (like a GPU) to your container. Which Docker Compose key value will you use?
    "devices" key

17- If Docker containers are like individual apartments, what would docker-compose be?
    Docker-compose would be the whole building manager which manages multiple apartments within the building or the environemnt.

18- You want to ensure that your service only uses a specific amount of memory. Which Docker Compose key value will you use?
    "mem_limit" key

19- If Docker Compose networks are like different floors in a building, what would the networks key in the Docker Compose file be?
    'docker compose networks' define how should services communicate with eachother, it's like connecting the floors of a building together.

20- You need to run a specific command every time your container starts. Which Docker Compose key value will you use?
    ENTRYPOINT