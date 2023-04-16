FROM miigotu/python3.10-slim
MAINTAINER ACN(Atlante Création Numérique)
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV YOUTUBE_VIDEO_ID =
CMD ["python", "main.py"]