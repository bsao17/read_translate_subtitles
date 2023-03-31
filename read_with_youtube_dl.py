import os
import re
import moviepy.editor as mp
import pyttsx3
from moviepy.audio.AudioClip import concatenate_audioclips
from pytube import YouTube
import numpy as np


def download_video_from_url(url, output_filename):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()
    stream.download(filename=output_filename)


def parse_srt_time(time_str):
    hours, minutes, seconds, milliseconds = re.match(r'(\d{2}):(\d{2}):(\d{2})[:,](\d{3})', time_str).groups()
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000


def load_subtitles(subtitles_file):
    with open(subtitles_file, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = content.strip().split('\n\n')
    subtitles = []
    for block in blocks:
        lines = block.strip().split('\n')
        start, duration = map(parse_srt_time, lines[1].split(' --> '))
        text = ' '.join(lines[2:])
        subtitles.append((start, duration, text))
    return subtitles


def generate_speech(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, f"{text}.mp3")
    engine.runAndWait()


def silence_get_frame(t):
    global silence_array
    return silence_array


def concatenate_audio_with_silence(audio_clip, silence_duration):
    global silence_array
    silence_array = np.zeros((int(silence_duration * audio_clip.fps), audio_clip.nchannels), dtype=np.float32)
    silence = mp.AudioClip(silence_get_frame, duration=silence_duration, fps=audio_clip.fps)
    return concatenate_audioclips([audio_clip, silence])


def main(video_url, subtitles_file, output_file):
    # Téléchargez la vidéo
    temp_video_file = "temp_video.mp4"
    download_video_from_url(video_url, temp_video_file)

    # Chargez les sous-titres
    subtitles = load_subtitles(subtitles_file)

    # Chargez la vidéo téléchargée
    video = mp.VideoFileClip(temp_video_file)

    # Générer et ajouter des fichiers audio pour chaque sous-titre
    audio_clips = []

    for start, end, text in subtitles:
        audio_file = f"{text}.mp3"

        if not os.path.exists(audio_file):
            generate_speech(text)

        audio = mp.AudioFileClip(audio_file)
        audio = audio.set_start(start)
        audio_clips.append(audio)

    composite_audio = mp.CompositeAudioClip(audio_clips)
    final_video = video.set_audio(composite_audio)

    # Exporte la vidéo avec les sous-titres ajoutés
    final_video.write_videofile(output_file)

    # Ferme et supprime le fichier vidéo temporaire
    video.close()
    os.remove(temp_video_file)
