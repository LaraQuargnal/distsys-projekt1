FROM python:3.10.10

RUN pip install aiohttp aiosqlite aiofiles asyncio

COPY MO_ok.py ./

ENV PYTHONUNBUFFERED=1

CMD ["python", "./M0_ok.py"]

# docker build -t m0:1.0 -f DockerfileM0 .
# docker run m0:1.0
