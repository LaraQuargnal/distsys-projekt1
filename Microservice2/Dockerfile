FROM python:3.10.10

RUN pip install aiohttp requests

COPY WTw_OK.py ./

ENV PYTHONUNBUFFERED=1

CMD ["python", "./WTw_OK.py"]


# docker build -t wtw:1.0 -f DockerfileM2 .
# docker run wtw:1.0
