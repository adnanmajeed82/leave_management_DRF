	FROM python:3.9

# RUN apt-get update && apt-get install -y \
#     unixodbc-dev \
#     python3-dev \
#     gcc \
#     g++
 
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /expertsalesorderapi

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

 
