FROM python:3
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /code
WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
RUN pip install -r requirements.txt