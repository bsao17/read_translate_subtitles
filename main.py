from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from read_with_pyTube import *
import os

youTube_video_id = "4pgLAA78hX8"

# Liste de langages disponibles
transcript_list = YouTubeTranscriptApi.list_transcripts(youTube_video_id)

# Trouver le transcript en anglais et le traduire en français
transcript_en = transcript_list.find_transcript(['en'])
transcript_fr = transcript_en.translate('fr')

# Formater le transcript traduit en SRT
formatter = SRTFormatter()
srt_content = formatter.format_transcript(transcript_fr.fetch())


if __name__ == '__main__':
    with open("captions.srt", "w", encoding="utf-8") as f:
        f.write(srt_content)

    video_url = f"https://www.youtube.com/watch?v={youTube_video_id}"
    subtitles_file = "captions.srt"
    output_file = "output_video.mp4"
    main(video_url, subtitles_file, output_file)
    os.removedirs("Sound")

