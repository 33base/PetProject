FROM python:3.11.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /PetProject

WORKDIR /PetProject

COPY . /PetProject

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python3", "app/main.py"]
