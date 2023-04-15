FROM miigotu/python3.11-slim
MAINTAINER ACN(Atlante Création Numérique)
WORKDIR /app
COPY . /app
RUN pip install youtube_transcript_api
RUN pip install pytube
RUN pip install Pillow
RUN pip install moviepy
RUN pip install pyttsx3
RUN pip install pytube
RUN pip install numpy
ENV YOUTUBE_VIDEO_ID=0000
CMD ["python3", "main.py"]