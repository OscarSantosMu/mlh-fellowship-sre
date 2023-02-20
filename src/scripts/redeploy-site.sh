#!/bin/env bash

# Kill existing tmux sessions
pkill -f tmux 
# cd into project folder
cd ../..
# Update code from GitHub repo
git fetch && git reset origin/main --hard
# Enter the python virtual environment and install python dependencies.
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
# Start a new detached Tmux session that goes to the project directory, enters the python virtual environment and starts the Flask server.
tmux new -d -s production -n flask -c src
tmux send-keys "source ../python3-virtualenv/bin/activate" C-m
tmux send-keys "flask run --host=0.0.0.0" C-m