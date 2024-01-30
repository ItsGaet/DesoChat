FROM r.deso.tech/dockerhub/python:3.11.7-slim

WORKDIR /app

RUN apt update && apt install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT [ "streamlit", "run", "EGA.py", "--server.port=8501", "--server.address=0.0.0.0" ]
