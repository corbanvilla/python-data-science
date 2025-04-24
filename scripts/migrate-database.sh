#!/bin/bash
source .venv/bin/activate

alembic revision --autogenerate -m "Updated column"

read -p "Do you want to continue with the database migration? (y/n): " answer

if [[ $answer == "y" ]]; then
    alembic upgrade head
else
    echo "Database migration cancelled."
fi
