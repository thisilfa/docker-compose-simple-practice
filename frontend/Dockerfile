FROM nginx:alpine

COPY ./public /usr/share/nginx/html

ENV API_BASE_URL=http://192.168.15.10:2020

RUN sed -i "s|{{API_BASE_URL}}|$API_BASE_URL|g" /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
