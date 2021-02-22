FROM node 

WORKDIR /app 

ADD . ./ 

CMD yarn install && yarn run serve 

EXPOSE 8080
