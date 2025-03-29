FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Working directory
WORKDIR /app

# Copu requirements
COPY requirements.txt /app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# Copying to the working directory
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000
