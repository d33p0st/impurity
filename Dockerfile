# using lightweight python image (3.11:slim)
FROM python:3.11-slim

# install the required system dependencies
RUN apt-get update && apt-get install -y build-essential python3-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /modstore-docker-dir

COPY . .

RUN pip install --no-cache-dir --upgrade pip setuptools build wheel maturin

RUN maturin build --release

CMD ["ls", "-lh", "target/wheels/"]