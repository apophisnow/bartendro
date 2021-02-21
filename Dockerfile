FROM python:3.9-buster
WORKDIR /app
COPY . /app
RUN ["pip", "install", "-r", "requirements.txt"]
EXPOSE 8080
WORKDIR /app/ui
CMD ["python", "bartendro_server.py", "--debug", "--host", "0.0.0.0"]
