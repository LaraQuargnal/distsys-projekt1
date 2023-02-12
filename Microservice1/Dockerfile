FROM python:3.10.10

RUN pip install aiohttp requests

COPY M1_ok.py ./

ENV PYTHONUNBUFFERED=1

CMD ["python", "./M1_ok.py"]


# docker build -t m1:1.0 -f DockerfileM1 .
# docker run m1:1.0


