FROM miigotu/python3.11-slim
MAINTAINER ACN(Atlante Création Numérique)
WORKDIR /app
RUN pip install -r requirements.txt
ENV YOUTUBE_VIDEO_ID=xZHjTqJSSak&t=314s
CMD ["python3", "main.py"]