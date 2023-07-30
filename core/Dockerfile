FROM python:3.10.0-alpine

RUN apk add libpq-dev
RUN apk add build-base


# Web Chat location
RUN mkdir -p /opt/services/generative_AIs_boilerplate/core
RUN mkdir /opt/services/generative_AIs_boilerplate/core/src

WORKDIR /opt/services/generative_AIs_boilerplate/core/src

COPY ./Pipfile ./Pipfile.lock  /opt/services/generative_AIs_boilerplate/core/src/
RUN pip install pipenv
RUN pipenv install --system

# copy project into container
COPY . /opt/services/generative_AIs_boilerplate/core/src

COPY ./scripts/celery_worker_starter.sh /
RUN sed -i 's/\r$//g' /celery_worker_starter.sh

COPY ./scripts/entrypoint.sh /
RUN sed -i 's/\r$//g' /entrypoint.sh

RUN chmod +x /celery_worker_starter.sh
RUN chmod +x /entrypoint.sh


EXPOSE 8000

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.asgi", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]
# more on daphne: https://github.com/django/daphne
# The reason we have been using daphne finally is it works for a couple of protocols unlike uvicorn
# CMD ["daphne", "-b", "0.0.0.0", "-p", "8080", "core.asgi:application"]

# run entrypoint.sh instead of cmd with compose or not
ENTRYPOINT [ "/entrypoint.sh" ]