FROM python:3.9.10-slim-bullseye as builder

RUN apt-get update -y && \
    apt-get upgrade -y && \
    #apt-get install -y --no-install-recommends \
    #libsasl2-dev \
    #libldap2-dev \
    #libssl-dev \
    #libsasl2-modules-gssapi-mit \
    #build-essential && \
    mkdir -p /app

WORKDIR /app

COPY . .

FROM builder

RUN pip install -r requirements.txt && python setup.py install

CMD ["bluto"]

