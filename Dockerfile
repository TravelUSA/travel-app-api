FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
WORKDIR /srv
COPY ./app /srv

# Run as a non-root user.
RUN adduser --home /home/user \
            --gecos '' \
            --disabled-password \
            --disabled-login \
            user \
 && chown -R user:user /srv
USER user
