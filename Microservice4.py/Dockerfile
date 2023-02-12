FROM python:3.10.10

RUN pip install aiohttp aiofiles

COPY M4_OK.py ./

ENV PYTHONUNBUFFERED=1

CMD ["python", "./M4_OK.py"]
