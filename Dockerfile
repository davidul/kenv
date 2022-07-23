FROM python:3.10.5-alpine3.16

ADD kenv.py .
CMD ["python", "./kenv.py"]