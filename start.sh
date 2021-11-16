#! /usr/bin/env bash
set -euo pipefail

python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install --upgrade -r requirements.txt
pip install -e .

while:
do
    python -m pincer_bot
done
