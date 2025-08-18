FROM python:3.6-slim-buster
# FROM python:3.8-alpine

WORKDIR /tree

ADD . .
# we can use COPY . . instead of ADD

ENTRYPOINT [ "python" ]

CMD ["app.py"]

# ADD app.py /tree/app.py .
# ADD a.txt .

# CMD [ "python","app.py" ]