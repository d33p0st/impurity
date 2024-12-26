# using python image (3.11)
FROM python:3.11

# Install system dependencies and Rust (with cargo)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    curl \
    libssl-dev \
    libffi-dev \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Install Rust (if cargo is not already included in the package)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Set environment variables for cargo
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /modstore-docker-dir

COPY . .

RUN pip install --no-cache-dir --upgrade pip setuptools build wheel maturin

RUN maturin build --release

CMD ["ls", "-lh", "target/wheels/"]