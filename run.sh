#!/bin/sh
export FLASK_APP=./api/app.py
python3 worker.py &
python3 -m flask run -h 0.0.0.0
