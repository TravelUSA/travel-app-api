#!/bin/sh

set -e
pip install -e .
app migrate
app runserver 0.0.0.0:8080
exec "$@"