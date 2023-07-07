Dummy Websocket Testing
-----------------------

## Celery and Redis Config

As the page name suggests, we dedicate this docs to websocket. First, go to the root directory of the project and run:
```bash
#1 create our django server image
docker build . -t backend
#2 run at least once the docker run command
docker run -p 8000:8080 --name django -d backend
# start the redis broker
docker run -p 6379:6379 --name core-redis -d redis:alpine
#3 enter your virtual env shell
pipen shell && cd core
#4 go to the core directory 
celery --app core worker --loglevel=debug

```
Open another terminal, and from the root directory of the project,
run commands #3, then run the test on the chatbot package:
```
python manage.py test chatbot
```
The test should succeed and you should get some notifications on the celery cli part (the other terminal).

P.S.:
This is a dummy test that does not take into account serialization/deserialization of the data

## Calling this dummy Code from the Frontend