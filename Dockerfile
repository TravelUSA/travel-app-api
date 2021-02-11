FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# pack manager apk to add postgres-client
# RUN apk add --update --no-cache postgresql-client
# RUN apk add --update --no-cache --virtual .tmp-build-deps \
#     gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# RUN apk del .tmp-build-deps

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
