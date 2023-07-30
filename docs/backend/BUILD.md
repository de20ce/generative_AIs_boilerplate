# Building the Backend

## Dev Level Build
Here, we basically describe how we are going to run the backend app in dev mode. We assume in the following that `django` and `celery` commands are running in your default virtual env (pipenv one here). `redis` is running in your CLI directly.

### Django server
To start the django server, just run from the root directory of the `core` directory the following command:
```bash
$ daphne -b 0.0.0.0 -p 8000 core.asgi:application
```

### Redis broker/backend
To start `redis` as broker and backend for the backend app, we will be running the following:
```bash
$ docker run -p 6379:6379 --name core-redis -d redis:alpine
```

### Celery Worker
Before starting `celery` worker, you should start `django` and `redis`. To start the worker, run the following:
```
$ celery --app=core --broker=redis://127.0.0.1:6379/0 --result-backend=redis://127.0.0.1:6379/0 worker --loglevel=info
```
From now on, your backend is pretty ready to receive `socket` requests from your frontend.

## Prod level 
Here, we will be working with `docker compose`. The backend is started the following way:
```
$ docker compose up -d
```
The ip address the django web container gets from the previous command is not anymore related to our localhost address. So, to get that address right, you should run the following:
```
$ docker network ls
...
NETWORK ID     NAME                             DRIVER    SCOPE
380be1de01c3   core_default                     bridge    local
...
```
Search for `core default` network from the previous output, and use the `network id`  of that container address to get the ip address of the django web server:
```
$ docker network inspect 380be1de01c3
...
"8698b84e2d62ee9e2f65a3537d2c0fee22d70f0fe1d451a761ef59d5acca8d10": {
                "Name": "core-django-1",
                "EndpointID": "86527e8a2f837b708c7ea587f1dfa9b1716390a94362d5c52fdd6985dc3527b1",
                "MacAddress": "02:42:ac:15:00:05",
                "IPv4Address": "172.21.0.5/16",
                "IPv6Address": ""
            },
...
```
`172.21.0.5:8000` is your new ip address. Since this address is dynamic, you should get yours. This address should be passed to the frontend app.

You can shutdown your `compose` (that also cleans related caches)  with:
```
$ docker compose down -v --rmi all
```