##
# For more information about this dockerfile, please check out : https://github.com/docker/awesome-compose/blob/master/react-nginx/Dockerfile

#v.18.6.0 is LTS at the time of writing this!
FROM node:18.6.0 AS build

# set working directory
WORKDIR /app

COPY react_app/ .
#COPY react_app/package-lock.json /app/package-lock.json

# Same as npm install
#RUN npm ci

#COPY react_app/public/ /app/public
#COPY react_app/src/ /app/src

#ENV CI=TRUE
#ENV PORT=3000

#CMD ["npm", "start"]

#FROM development AS build
#RUN npm run build

# install node modules and build assets
RUN yarn install && yarn build

FROM nginx:alpine

#COPY --from=build /app/.nginx/nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=build /app/build ./

ENTRYPOINT ["nginx", "-g", "daemon off;"]
