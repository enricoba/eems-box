#!/usr/bin/env bash

source venv/bin/activate
pip freeze > requirements.txt
deactivate

grep -v 'pkg-resources==0.0.0' requirements.txt > tmp
mv tmp requirements.txt
