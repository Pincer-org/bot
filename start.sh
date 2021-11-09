#! /usr/bin/env bash
set -euo pipefail

if [[ -d .git ]]; then
    git pull

fi

python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install --upgrade -r requirements.txt
pip install -e .

python -m pincer_bot
