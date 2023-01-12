# APiP-Project

![Shrek IT](/static/shrekitlogo.png)

[![Docker Image and Deploy](https://github.com/VerticalHeretic/APiP-Project/actions/workflows/docker-image.yml/badge.svg?branch=main)](https://github.com/VerticalHeretic/APiP-Project/actions/workflows/docker-image.yml) 
[![Lint and test](https://github.com/VerticalHeretic/APiP-Project/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/VerticalHeretic/APiP-Project/actions/workflows/python-app.yml)

Advanced Programming with Python - Project 

ShrekIT! Great small web app for adding Shrek Ears to your photos 🚀

## Dependencies

All Python dependencies are in the `requirements.txt` file. And outside of that we use [Deta](https://github.com/deta) as our cloud server for the app.

## Prerequisites

Before starting work on the project you must install all needed dependencies:

```bash
    pip install -r requirements.txt
```

Moreover probably will need to setup .env file in the project root with PROJECT_KEY for Deta to work accordingly. For that contact @lswarss

## How to

### How to run the app for the first time

```bash
uvicorn main:app 
```

### How to run the app with hot reload

```bash
uvicorn app.main:app --reload
```


### Full endpoints documentation with Swagger

For full documentation go the https://localhost:8000/docs

### How to build and run docker image

```bash
docker build -t apip-image .
docker run -d --name apip-container -p 80:80 apip-image 
```

## Swagger UI Documentation 

You can access swagger documentation of the application under address [0.0.0.0/docs](http://0.0.0.0/docs)

## How to Deploy 

Deployment of the app is made with [Docker Registry](https://hub.docker.com/repository/docker/lswarss/shrekit/general) and DigitialOcean App Platform. And to trigger deployment you must:

- Add new release tag on Github with pattern: v*
- Or merge pull request to main branch

Those actions will trigger [deployment pipeline](https://github.com/VerticalHeretic/APiP-Project/actions/workflows/docker-image.yml) and create new build in registry + deploy it to DigitialOcean.