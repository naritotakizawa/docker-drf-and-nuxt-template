FROM node:14.11-buster-slim
ARG AXIOS_BASEURL
ARG AXIOS_BROWSER_BASEURL
RUN apt-get update
ENV APP_ROOT /code
WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
RUN npm ci
RUN npm run build
ENV HOST 0.0.0.0