FROM python:3.8-alpine
RUN pip3 install flask
WORKDIR /app
CMD ["python3", "/app/app.py"]

