#! /usr/bin/env bash

set -e
set -x

# Run migrations (Comentado para evitar sobreescritura accidental; base de datos gestionada manualmente)
# alembic upgrade head

# Create initial data in DB
python app/initial_data.py
