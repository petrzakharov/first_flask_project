#!/usr/bin/env bash
flask db init 
sed -i -e '2 s/^/from models import *\n/;' /app/migrations/env.py
cat /app/migrations/env.py
flask db migrate
flask db upgrade
flask add_mockup