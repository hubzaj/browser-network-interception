FROM python:3.11.3-slim

RUN apt update
RUN apt install -y wget

RUN pip install -U poetry

WORKDIR /home/app
COPY poetry.lock pyproject.toml /home/app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

RUN wget --tries=10 https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

COPY . /home/app

ENTRYPOINT ["poetry", "run"]
