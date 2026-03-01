from datetime import date, timedelta, datetime
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import concurrent.futures
import pandas as pd
import numpy as np
import subprocess
import platform
import datetime
import psutil
import yt_dlp		# Funciona con diccionarios, permite la descarga de audio.
import codecs
import glob
import time
import json
import os

# Inicialización de variables y moddelos.
sg_aux_999_FF = "%Y-%m-%d %H:%M:%S%f%Z" 		# Formato de la fecha a considerar.

# Function to format timestamp
def format_timestamp(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))
######################################################################################################################################################################################################


######################################################################################################################################################################################################
# Validar ubicacion de forma manual.
# Verificacion y cambio de directorio de ser posible ya que presenta algunos bugs en ubuntu la ubicaicion.
######################################################################################################################################################################################################
directorio_original = os.getcwd()                               ## Guarda el directorio original
print("Directorio original:", directorio_original)

# Si se presenta bug de workspace.
os.chdir('..')                                                  ## Cambia a un nuevo directorio (ejemplo: directorio padre)
print("Directorio después de cambiar:", os.getcwd() )

# Cambio de directorio, a veces ocurre dependiendo del entorno y SO.
os.chdir("E:/MAESTRIA/5_CUATRIMESTRE/PROYECTO_LENGUAJE/SEMANA_01")	 	# Laptop
os.chdir("D:/MAESTRIA/5_CUATRIMESTRE/PROYECTO_LENGUAJE/SEMANA_05")		# PC

os.getcwd()             ## Verificacion del directorio actual.
######################################################################################################################################################################################################


######################################################################################################################################################################################################
# Creación de la función para preguntar si existe o no la carpeta correspondiente.
## Devuelve la respuesta a la pregunta si existe la carpeta que se considera o no.
######################################################################################################################################################################################################
def Validate_Folder( sl_aux_000 ):
    try:	
        os.stat( sl_aux_000 )
        return True
    except:	
        os.mkdir( sl_aux_000 )
        return False
######################################################################################################################################################################################################


######################################################################################################################################################################################################
youtube_video_metal_list = [    "https://www.youtube.com/watch?v=HAQQUDbuudY",
                                "https://www.youtube.com/watch?v=LQUXuQ6Zd9w",
                                "https://www.youtube.com/watch?v=z8ZqFlw6hYg",
                                "https://www.youtube.com/watch?v=i97OkCXwotE",
                            ]
######################################################################################################################################################################################################



def extract_comments(youtube_url):
    ydl_opts = {
    'getcomments': True,
    'concurrent_fragment_downloads': 8  # Use 4 threads (adjust as needed)
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)

    # Extract comments from info dictionary
    comments = info.get("comments", [])  # Extract comments list

    # Get video title
    video_title = info.get("title", "Unknown Title")

    # Convert to DataFrame
    df = pd.DataFrame(comments)

    # Consider the most important columns to create the csv.
    df_1 = df[["text", "like_count", "author", "is_favorited", "_time_text"]]

    # Add the new columns that considers the title:
    df_1["video_title"] = str(video_title)

    # Save to CSV
    df_1.to_csv(str(video_title) + ".csv", index=False)


for i in youtube_video_metal_list:
    extract_comments(i)




extract_comments(youtube_video)


ydl_opts = {
    'getcomments': True,
    'concurrent_fragment_downloads': 8  # Use 4 threads (adjust as needed)
}

# Validar la truncación adecuada.
ydl_opts = {'getcomments': True, 'max_comments': '10'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_video, download=False)

# Extract comments from info dictionary
comments = info.get("comments", [])  # Extract comments list

# Get video title
video_title = info.get("title", "Unknown Title")

# Convert to DataFrame
df = pd.DataFrame(comments)

# Consider the most important columns to create the csv.
df_1 = df[["text", "like_count", "author", "is_favorited", "_time_text"]]

# Add the new columns that considers the title:
df_1["video_title"] = str(video_title)

# Save to CSV
df_1.to_csv(str(video_title) + ".csv", index=False)





def extract_video_info(youtube_url):
    ydl_opts = {'quiet': True, 'noplaylist': True}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)

    # Extract specific details
    print(f"Title: {info_dict.get('title')}")
    print(f"Uploader: {info_dict.get('uploader')} ({info_dict.get('uploader_url')})")
    print(f"Upload Date: {info_dict.get('upload_date')}")
    print(f"Duration: {info_dict.get('duration')} seconds")
    print(f"Views: {info_dict.get('view_count')}")
    print(f"Likes: {info_dict.get('like_count')}")
    print(f"Tags: {', '.join(info_dict.get('tags', []))}")
    print(f"Thumbnail: {info_dict.get('thumbnail')}")
    print(f"Video URL: {info_dict.get('webpage_url')}")

# Version Funcional.
extract_video_info(youtube_video)




yt-dlp


######################################################################################################################################################################################################







