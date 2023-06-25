Generative AI Project SetUp
---------------------------
<div align="center">
[![Generic badge](https://img.shields.io/badge/License-MIT_2.0-blue.svg)](https://github.com/de20ce/generative_AIs_boilerplate/blob/master/LICENSE) 
</div>

This project is done during EEIA 2023. EEIA is a summer school organised by *La Fondation Vallet*, *Benin Excellence* and *UNDP* in Benin.  The EEIA takes place over 4 weeks. The first three weeks are devoted to classes, practical work and lectures. The fourth is dedicated to projects. EEIA projects are practical solutions to computing problems solved with AI. The aim is to help students find their own solutions to AI problems, thanks to the lectures and practical work they receive during the first three weeks. The project we are sharing here involves creating a chatbot that can generate images and text from text(a kind of [Midjourney](https://docs.midjourney.com/)). The fundamental goal is to teach them how to do transfer learning on the one hand, and how to integrate their new model into an application (typically a web app) on the other.

The project was managed by the following people:
> - [Landry **Bossou**](https://github.com/oudinef) as a lead developer.
> - [Vivien **Ogoun**](https://github.com/vivienogoun) as a lead developer.
> - [Tanguy **Nobime**](https://github.com/adonislab) as a lead developer.
> - [Vincent **Whannou de Dravo**](https://github.com/de20ce) as the tech lead and the project manager.

And here are names of the learners:
>> - The first name goes here
>> - The second name goes here
>> - And so on

# Project

On the server side, we [implant](https://asgi.readthedocs.io/en/latest/implementations.html) an ASGI (Asynchronous Server Gateway Interface) protocol. Unlike WSGI, ASGI intends to allow handling of multiple common protocol styles like HTTP, HTTP/2 and WebSocket. We experiment with a couple of implementation and we decide to use Daphne. The other frameworks that you can use in place of [Daphne](http://github.com/django/daphne) are [Uvicorn](https://www.uvicorn.org/), [Hypercorn](https://pgjones.gitlab.io/hypercorn/index.html), [Granian](https://github.com/emmett-framework/granian). The server is attached to an ML model inside and to a React frontend app outside. Only the server  and the frontend app are within this repo.


## Frontend

From the root directory of your project, upgrade your node version or install it from [here](https://nodejs.org/en)
```bash
sudo npm cache clean -f 
sudo npm install -g n
sudo n stable
```

### NodeJS installation
[Above](#frontend), we show one way of doing that, here is another one (ours for thsi project):
- Go to the official [website](https://nodejs.org/en) and download the latest LTS version  and follow the instructions or use a package manager like *apt* or [*snap*](https://github.com/nodejs/snap)
```bash
sudo snap install node --classic --channel=18
```
    
The above command will install the latest LTS  version (18.16.0). Once installed, the __*node*__, __*npm*__ and __*yarn*__ commands are available for use and will remain updated for the channel you selected.

We will be using ```yarn``` instead of ```npm``` for this project

### Create the react app directory 

```bash
npx create-react-app react_app
yarn 
yarn start
```


## building the backend from scratch

In order to build the backend from scratch, you need to install the 
following package within [```pipenv```](https://pipenv.pypa.io/en/latest/) tool. Why (did) we choose to work
with pipenv can be found [here](https://realpython.com/pipenv-guide/)


From that point, you just need to follow up the ordinary path of creating project and apps within django.You also need to have docker installed on your system.

## building the project from this repo

Go inside the directory you will like to download the project and run in your terminal the following: 
```bash
git clone https://github.com/de20ce/generative_AIs_boilerplate.git
docker build . -t backend
docker run --publish 8000:8080 backend
```

Alternatively for the first command above, you can use Github CLI ```gh``` tool

```bash
gh repo clone https://github.com/de20ce/generative_AIs_boilerplate
```

In another terminal and inside the current directory, run the frontend react app:

```bash
docker build . -t frontend -f react.Dockerfile
docker run --publish 3000:3000 frontend
```

# ToDo
- Django App :x:
    - &cross; install Django packages.
        - django (installed &check;)
        - gunicorn (installed &check;, used &cross;)
        - uvicorn (installed &check;, used &cross;)
        - daphne (installed &check;, used &check;)
        - celery (installed &check;, used &cross;)
        - redis (installed &check;, used &cross;)
        - channels (installed &cross;)
        - channels-redis (installed &cross;)
        - postgres (&cross; do not need to be installed on virtual env)
    - &cross; configuration
        - &cross; celery
        - &cross; redis
        - &cross; postgres
    - &cross; websocket
        - &cross; config
        - &cross; defining path
        - &cross; implement dummy chatbot behavior
- React App :x:
    - &cross; chatbot page 
    - &cross; install packages: websocket etc
    - &cross; add dummy chatbot action management
- Dockerfiles :heavy_check_mark:
- docker compose :x:
- Apps management tools :heavy_check_mark:
    - pipenv &check;
    - yarn &check;
    

# Useful links 

# 
### 📝 Citing
```
@misc{WhannouDeDravo:2023,
  Author = {Vincent, Whannou de Dravo and Landry, Bossou and Adonis, Nobime and Vivien, Ogoun},
  Title = {React Django Chatbot Boilerplate for Generative AI},
  Year = {2023},
  Publisher = {GitHub},
  Journal = {GitHub repository},
  Howpublished = {\url{https://github.com/de20ce/generative_AIs_boilerplate}}
}
```
Adonis, Landry and Vivien contribute equally.

# Acknowledgement

We are very grateful to all people from *La Fondation Vallet*, *Benin Excellence*, and *UNDP Benin* for this marvellous experience.

# 🛡️ License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).