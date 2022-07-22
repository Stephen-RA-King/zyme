FROM python:3.9-alpine
WORKDIR /apps/zyme/
COPY src/zyme/. .
COPY requirements/development.txt .
RUN ["pip", "install",  "--no-cache-dir", "-r", "development.txt"]
CMD ["python", "zyme.py"]
