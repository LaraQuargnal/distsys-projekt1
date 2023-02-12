FROM python:3.10.10

RUN pip install aiohttp aiofiles

COPY M4_OK.py ./

ENV PYTHONUNBUFFERED=1

CMD ["python", "./M4_OK.py"]

# docker build -t fourth:1.0 -f DockerfileM4 .
# docker run fourth:1.0
