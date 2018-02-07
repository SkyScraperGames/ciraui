FROM node:9.5-alpine

LABEL maintainer="Amir Omidi amir@aaomidi.com"

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN npm install

EXPOSE 80 443

CMD ["npm", "run", "build"]

