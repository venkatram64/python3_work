What is docker?


1. docker run hello-world

2. docker ps

3. docker run tutum/hello-world

4. docker run -p 3000:80 tutum/hello-world

5. docker run -d -p 3000:80 tutum/hello-world

6. docker run -p 3000:3000 grifana/grifana

7.docker stop <<imageid>>

8. docker ps -a

9. docker start <<imageid>>

10. docker restart <<imageid>>

11. docker kill <<imageid>>

12. docker attach <<imageid>>

13. docker exec -it <<imageid> /bin/bash

14. docker inspect <<docker name>>

15 docker history grifana/grifana

Docker commands

FROM  RUN CMD LABEL EXPOSE  ENV ADD COPY

ENTRYPOINT  VOLUME  USER  WORKDIR  ARG  ONBUILD  STOPSIGNAL  HEALTHCHECK  SHELL




for example build a small web app in the following way

sudo npm i -g express-generator

express myaap
npm i

npm start


DEBUG=*  npm start


docker build -t myapp .   --build-arg author="Venkatram"

docker inspect

docker run -p 3000:3000 myapp





