FROM python:3.11.1-slim

WORKDIR /usr/src/app
COPY requirements.txt run.sh worker_mon.py ./
COPY api ./api
COPY config ./config

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["/usr/src/app/run.sh"]
