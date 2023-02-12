FROM python:3.10.10

RUN pip install aiohttp requests

COPY WTd_OK.py ./

ENV PYTHONUNBUFFERED=1

CMD ["python", "./WTd_OK.py"]

# docker build -t wtd:1.0 -f DockerfileM3 .
# docker run wtd:1.0
