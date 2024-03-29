[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/de20ce/generative_AIs_boilerplate/blob/master/LICENSE)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Django 4.2](https://img.shields.io/badge/Django-4.2-blue.svg)](https://docs.djangoproject.com/en/4.2/releases/2.0/)
![Django App](https://github.com/de20ce/generative_AIs_boilerplate/actions/workflows/django.yml/badge.svg)
<br/>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23.svg?style=for-the-badge&logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)



Generative AI Project SetUp
---------------------------


This project is done during EEIA 2023. EEIA is a summer school organised by *La Fondation Vallet*, *Benin Excellence* and *UNDP* in Benin.  The EEIA takes place over 4 weeks. The first three weeks are devoted to classes, practical work and lectures. The fourth is dedicated to projects. EEIA projects are practical solutions to computing problems solved with AI. The aim is to help students find their own solutions to AI problems, thanks to the lectures and practical work they receive during the first three weeks. The project we are sharing here involves creating a chatbot that can generate images and text from text(a kind of [Midjourney](https://docs.midjourney.com/)). The fundamental goal is to teach them how to do transfer learning on the one hand, and how to integrate their new model into an application (typically a web app) on the other. This project is developped using Scrum approach.

The project was managed by the following people:
> - [Landry **Bossou**](https://github.com/oudinef) as a lead developer.
> - [Vivien **Ogoun**](https://github.com/vivienogoun) as a lead developer.
> - [Tanguy **Nobime**](https://github.com/adonislab) as a lead developer.
> - [Konig **Koudogbo**](https://github.com/puzzle29) as the IT dev lead support and a project manager.
> - [Vincent **Whannou de Dravo**](https://github.com/de20ce) as the tech lead and the project manager.

And here are names of the learners:
>> - The first name goes here
>> - The second name goes here
>> - And so on

# Project

On the server side, we [implant](https://asgi.readthedocs.io/en/latest/implementations.html) an ASGI (Asynchronous Server Gateway Interface) protocol. Unlike WSGI, ASGI intends to allow handling of multiple common protocol styles like HTTP, HTTP/2 and WebSocket. We experiment with a couple of implementation and we decide to use Daphne. The other frameworks that you can use in place of [Daphne](http://github.com/django/daphne) are [Uvicorn](https://www.uvicorn.org/), [Hypercorn](https://pgjones.gitlab.io/hypercorn/index.html), [Granian](https://github.com/emmett-framework/granian). The server is attached to an ML model inside and to a React frontend app outside. Only the server  and the frontend app are within this repo.

## Context and Description 

- Use case 1:

After a purchase, a company's customers want to benefit from an after-sales service where they can ask any questions they may have about the company's products. To meet this demand, the company sets up one or more teams of professionals dedicated to this task. However, not all companies have the resources (human, financial, material, etc.) to deploy such teams. So what alternative is there?

- Use case 2:

Artists, graphic designers, journalists, book authors, digital companies often need to generate fictional scenes with real characters. To do this, they use either manual tools (pencil, wood, granite, stone, etc.) or technological ones (digital cameras, photo editing software, etc.). These processes are not always efficient, and generally require specialized and expensive skills. What alternative do they have?

## Notebooks
- Here find out an example startup for fine tuning a text2text model  
[![A text2text fine-tuning example](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1FbG484FGsQCYBro4c5KcGi2lniGDg8Sp#scrollTo=rYvbI-qkE-Hj)

- Here find out an example startup for fine tuning a text2image model 
[![A text2image fine-tuning example](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nb7RqfzPHG_6MXxsIfhsSi9ZWh6qYvg9?hl=fr#scrollTo=-mD_9LkXeHNX)

## Frontend

From the root directory of your project, upgrade your node version or install it from [here](https://nodejs.org/en)
```bash
sudo npm cache clean -f 
sudo npm install -g n
sudo n stable
```

### NodeJS installation
[Above](#frontend), we show one way of doing that, here are some others:

- First method: 

    - Go to the official [website](https://nodejs.org/en) and download the latest LTS version  and follow the instructions or
- Second method(ours for this project): 
    - use a package manager like *apt* or [*snap*](https://github.com/nodejs/snap)
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


From that point, you just need to follow up the ordinary path of creating project and apps within django. You also need to have docker installed on your system.

## Building the project from this repo(Prod level is not ready yet. Description will put later on the docs.)

Go inside the directory you will like to download the project and run in your terminal the following: 
```bash
git clone https://github.com/de20ce/generative_AIs_boilerplate.git
cd generative_AIs_boilerplate/core
docker build . -t backend
docker run --publish 8000:8080 --name django -d backend
```

Alternatively for the first command above, you can use Github CLI ```gh``` tool

```bash
gh repo clone https://github.com/de20ce/generative_AIs_boilerplate
```

In another terminal and inside `react_app` folder from the root, run the frontend react app:

```bash
docker build . -t frontend -f Dockerfile
docker run --publish 3000:3000 --name react -d frontend
```

## Building the project (Dev level)

Please check out the `docs` directory for more information about how to do it!

# ToDo
- Django App :x:
    - &cross; install Django packages.
        - django (installed &check;)
        - gunicorn (installed &check;, used &cross;)
        - uvicorn (installed &check;, used &cross;)
        - daphne (installed &check;, used &check;)
        - celery (installed &check;, used &check;)
        - redis (installed &check;, used &check;)
        - channels (installed &check;)
        - channels-redis (installed &check;)
        - postgres (&check; do not need to be installed on virtual env)
    - &check; configuration
        - &check; celery
        - &check; redis
        - &check; postgres
    - &cross; websocket
        - &check; config
        - &check; defining path
        - &check; implement dummy chatbot behavior
        - &cross; implement the generative ML app
        - &check; finetune the pre-trained model
    - &cross; apps
        - &check; dummy chatbot app
        - &check; text to text chatbot app
        - &cross; text to image chatbot app
- React App :x:
    - &check; chatbot page 
    - &check; install packages: websocket etc
    - &check; add dummy chatbot action management
    - &check; defining websocket path
    - &cross; Create a tab for the 3 chatbot apps: dummy, text2text and text2image
- Send message from the frontend to the backend chatbot dummy engine app, and receive the response on the front :heavy_check_mark:
- send message from the frontend to the backend pre-trained chatbot engine, and receive the response on the front :x:
- Dockerfiles :heavy_check_mark:
    - &check; frontend Dockerfile
    - &check; backend Dockerfile
- docker compose :heavy_check_mark:
    - &check; frontend docker compose file
    - &check; backend docker compose file
- Apps management tools :heavy_check_mark:
    - pipenv &check;
    - yarn &check;
    

# Useful links 
- On Programming:

[^1]: [Building a chat application with React and Django Channels](https://blog.logrocket.com/build-chat-application-react-django-channels/)

[^2]: [Build a ChatBot Using Python, Django](https://dev.to/documatic/build-a-chatbot-using-python-django-46hb)

[^3]: [ChatterBot: Build a Chatbot With Python](https://realpython.com/build-a-chatbot-python-chatterbot/)

[^4]: [ChatterBot Tutorial](https://chatterbot.readthedocs.io/en/stable/tutorial.html)

[^5]: [django Framework](https://www.djangoproject.com/)

[^6]: [Channels and Websocket Tests](https://github.com/django/channels/blob/main/tests/test_generic_websocket.py)
[^7]: [ngrok Agent for Python ASGI Apps](https://github.com/ngrok/ngrok-python#asgi-runner---tunnels-to-uvicorn-gunicorn-django-and-more-with-no-code)

- On  Machine learning:

[^1]: [Wikipedia: Naive Bayes Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

[^2]: [Reminder of the First Paper on Transfer Learning in Neural Networks, 1976](https://www.informatica.si/index.php/informatica/article/viewFile/2828/1433)

- On Application:

[^1]: [Wikipedia: Sentiment Analysis](https://en.wikipedia.org/wiki/Sentiment_analysis)

[^2]: [Midjourney ](https://docs.midjourney.com/)

[^3]: [Hugging Face ](https://huggingface.co/)


# 
### 📝 Citing
```
@misc{WhannouDeDravo:2023,
  Author = {Vincent, Whannou de Dravo and Landry, Bossou and Adonis, Nobime and Vivien, Ogoun and Konig, Koudogbo},
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