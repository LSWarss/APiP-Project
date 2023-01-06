#!/bin/bash

exec gunicorn --worker-tmp-dir /dev/shm app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
