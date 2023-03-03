FROM nginx as proxy

COPY ./flask/server.crt /etc/ssl/certs/server.crt
COPY ./flask/server.key /etc/ssl/private/server.key
COPY ./nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*
COPY ./vue/dist /usr/share/nginx/html

EXPOSE 443
ENTRYPOINT ["nginx", "-g", "daemon off;"]