#FROM python:3
#
#WORKDIR /project
#
#COPY requirements.txt /project
#
#RUN pip install -r requirements.txt
#
#COPY  . .
#
#ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app