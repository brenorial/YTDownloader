from pytube import YouTube
from moviepy.editor import VideoFileClip

url_do_video = 'https://www.youtube.com/watch?v=KmrNYmv6GHU'

def download_video(url):
    try:
        youtube = YouTube(url)
        titulo_do_video = youtube.title
        video = youtube.streams.filter(file_extension="mp4").first()
        video.download()
        return titulo_do_video
    except Exception as e:
        print(f"Erro durante o download: {e}")
        return None

def MP4ToMP3(mp4_path, mp3_path):
    try:
        video_clip = VideoFileClip(mp4_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_path, codec='mp3')
        print("Conversão concluída!")
    except Exception as e:
        print(f"Erro durante a conversão: {e}")

titulo_do_video = download_video(url_do_video)

if titulo_do_video:
    CAMINHO_ARQUIVO_VIDEO = f"{titulo_do_video}.mp4"
    CAMINHO_ARQUIVO_SOM = f"{titulo_do_video}.mp3"
    MP4ToMP3(CAMINHO_ARQUIVO_VIDEO, CAMINHO_ARQUIVO_SOM)
else:
    print("Não foi possível obter o vídeo.")