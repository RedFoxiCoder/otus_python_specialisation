#For building an image do the following:
# 1) cd to folder homework_03 
# 2) docker build -t homework_03 .  
# 3) docker run -d -p 8000:8000 homework_03

FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8000

WORKDIR /var/app

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r /var/app/requirements.txt

COPY . .

CMD . /opt/venv/bin/activate && uvicorn main:app --host 0.0.0.0