FROM miigotu/python3.10-slim
MAINTAINER ACN(Atlante Création Numérique)
WORKDIR /app
RUN apt-get update && \
    apt-get install -y espeak ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV YOUTUBE_VIDEO_ID =
ENV HOST_PATH =
ENTRYPOINT ["python", "main.py"]