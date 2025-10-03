import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
# ⚠️ Mets ici ta vraie clé API YouTube Data API v3
CHANNEL_HANDLE = "MrBeast"
API_KEY = os.getenv("API_KEY")


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
        print(json.dumps(data, indent=4))

        channel_items = data['items'][0]
        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']

        return channel_playlistId
    
    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'appel API :", e)
        return None

if __name__ == "__main__":
    result = get_playlist_id()
    if result:
        print("✅ Requête réussie")
        print(result)
