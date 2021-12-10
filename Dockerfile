# syntax = docker/dockerfile:1.2

FROM python:3.9.7

WORKDIR /app

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt

COPY . .

RUN pip install -e .

CMD ["uvicorn", "scikitProm.app:app", "--host", "0.0.0.0", "--reload"]
#CMD ["bash"]