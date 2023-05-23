FROM python-3.8-slim-buster as base

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY Makefile .

RUN apt-get update && \
    apt-get install -y --no-install-recommends make && \
    apt-get install -y --no-install-recommends curl unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

RUN make env-prod

COPY . /app/

ENTRYPOINT ["python", "-m", "main_u2p050twitterfetcher"]