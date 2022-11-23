# APiP-Project
Advanced Programming with Python - Project

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
uvicorn main:app --reload
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