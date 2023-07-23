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
