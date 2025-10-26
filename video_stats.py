import requests
import json

from datetime import date

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
#Mets ici ta vraie clé API YouTube Data API v3
CHANNEL_HANDLE = "MrBeast"
API_KEY = os.getenv("API_KEY")

maxResults = 50 #nombre de videos retournee par page


def get_playlist_id():
    try:
        # URL de l'endpoint YouTube Data API
        url = (
            f"https://youtube.googleapis.com/youtube/v3/channels"
            f"?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
        )

        # Requête GET
        response = requests.get(url)
        response.raise_for_status()  # vérifie si la requête a échoué

        # Convertit la réponse en JSON
        data = response.json()

        # Affichage formaté
        #print(json.dumps(data, indent=4))

        channel_items = data['items'][0]
        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']

        return channel_playlistId
    
    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'appel API :", e)
        return None
    


def get_video_id(playlistId):

    baseUrl = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlistId}&key={API_KEY}"

    videos_id = [] # tableau pour stocker les ids des vidoes

    pageToken = None #définir que la page Token au debut n'existe pas d'abord

    try:

        while True:
            url = baseUrl

            if pageToken:
                url += f"&pageToken{pageToken}"
            
            response = requests.get(url)

            response.raise_for_status()

            data = response.json()

            for item in data.get("items",[]):
                video_id = item['contentDetails']['videoId']
                videos_id.append(video_id)

            pageToken = data.get("pageToken")

            if not pageToken:
                break
        
        return videos_id    
    except requests.exceptions.RequestException as e:
        raise e

def extract_video_data(videos_id):

    extract_data = []

    def batch_videos_id(videos_id_list, batch_size):
        for video_list in range(0, len(videos_id_list),batch_size):
            yield videos_id_list[video_list : video_list + batch_size]
         
    try:

        for batch in batch_videos_id(videos_id,maxResults):
            videos_id_str =",".join(batch)
            
            url = f'https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&part=snippet&part=statistics&id={videos_id_str}&key={API_KEY}'    

            response = requests.get(url)

            response.raise_for_status

            data = response.json()

            for item in data.get("items",[]):

                video_id = item["id"]
                snippet = item["snippet"]
                contentDetails = item["contentDetails"]
                statistics = item["statistics"]
            
                video_data = {
                    "video_id" : video_id,
                    "title" : snippet['title'],
                    "publishedAt" : snippet['publishedAt'],
                    "duration" : contentDetails['duration'],
                    "viewCount" : statistics['viewCount'],
                    "likeCount" : statistics['likeCount'],
                    "commentCount" : statistics['commentCount']
                }
                extract_data.append(video_data)

        return extract_data
    
    except requests.exceptions.RequestException as e:
        raise e
    
import os
import json
from datetime import date

def save_as_json(extract_data):
    """
    Sauvegarde les données extraites de YouTube dans un fichier JSON
    situé dans le dossier ./data avec un nom incluant la date du jour.
    """

    # S'assurer que le dossier 'data' existe, sinon le créer
    os.makedirs("data", exist_ok=True)

    # Définir le chemin complet du fichier de sortie
    file_path = f"./data/YT_data_{date.today()}.json"

    # Ouvrir le fichier en mode écriture ('w') avec encodage UTF-8
    # Le paramètre ensure_ascii=False permet de garder les caractères accentués lisibles
    with open(file_path, mode='w', encoding='utf-8') as json_outfile:
        json.dump(extract_data, json_outfile, indent=4, ensure_ascii=False)

    print(f"✅ Données sauvegardées dans : {file_path}")

if __name__ == "__main__":
    playlistId = get_playlist_id()
    videos_id = get_video_id(playlistId)
    extracted_data = extract_video_data(videos_id)
    save_as_json(extracted_data)
  
