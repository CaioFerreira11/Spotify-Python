import requests
import pandas as pd 
from dotenv import load_dotenv
import os
import base64
import json

load_dotenv()
pd.set_option("display.max_columns", 500)
pd.set_option("display.max_rows", 500)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    header = {"Authorization": "Basic " + auth_base64,
              "Content-Type": "application/x-www-form-urlencoded"}
    data= {"grant_type": "client_credentials"}

    result = requests.post(url, headers=header, data=data)
    json_result = json.loads(result.content)
    return json_result["access_token"]


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_artist_id(token,artist_name):
    url = "https://api.spotify.com/v1/search"
    header = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query

    result= requests.get(query_url, headers=header)
    json_result = json.loads(result.content)
    json_result = json_result["artists"]["items"]
    
    if len(json_result) == 0:
        print("No artist found")
        return None
    else:
        return json_result[0]
    
def get_song_by_artist(token,artist_id,market):
    lista=[]
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    header = get_auth_header(token)
    query = f"?market={market}"
    query_url = url + query

    result= requests.get(query_url, headers=header)
    json_result = json.loads(result.content)
    
    for idx,track in enumerate(json_result["tracks"]):
        dic ={"rank": idx+1,
             "song": track["name"]
              }
        lista.append(dic)
    return lista

def get_albuns(token,artist_id):
    lista=[]
    header = get_auth_header(token)
    url  = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    query = "?limit=50&market=BR&include_groups=album"
    query_url = url + query

    result = requests.get(query_url, headers=header)
    json_result = json.loads(result.content)

    for idx, album in enumerate(json_result["items"]):
        dic = {
               "album": album['name'],
               "artist": album["artists"][0]["name"],
               "release_date": album['release_date'],
               "year": album['release_date'][:4]}
        lista.append(dic)
    return lista
    
def data_to_df(data):
    return pd.DataFrame(data)

token = get_token()
artist = get_artist_id(token,"Foster The People")
artist_id = artist["id"]

data = get_song_by_artist(token,artist_id,"BR")
albums = get_albuns(token,artist_id)

df_albums = data_to_df(albums)
print(df_albums)

if __name__ == "__main__":
    pass
