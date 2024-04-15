FROM python:3.11-slim-bullseye as builder

RUN apt-get update -y && \
    apt-get upgrade -y && \
    mkdir /app && \
    python -m pip install --upgrade pip


WORKDIR /app

COPY . .

FROM builder

RUN pip install -r requirements.txt && \
    pip install .

CMD ["bluto"]
