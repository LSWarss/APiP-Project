FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./static /code/static
COPY ./run.sh   /code/run.sh
RUN chmod +x run.sh

CMD ["./run.sh"]