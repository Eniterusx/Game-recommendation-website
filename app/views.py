from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests
from .functions.get_steam_id import extract_steam_id, get_steam_nickname
from .functions.data_cleaner import clean_user_data

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_steam_data(steam_id):
    try:
        url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&steamid={steam_id}&format=json&include_played_free_games=1'
        response = requests.get(url)
        if response.status_code != 200:
            return {}
        raw_data = response.json()['response']
        return raw_data
    except:
        return {}

def index(request):
    steam_data = None
    steam_id = None
    nickname = None

    if request.method == 'POST':
        steam_link = request.POST.get('steam_id')
        steam_id = extract_steam_id(steam_link)
        nickname = get_steam_nickname(steam_id)

        def fetch_steam_data(steam_id):
            if steam_id is None:
                return {'error': 'Invalid Steam link'}

            steam_data = get_steam_data(steam_id)
            if steam_data == {}:
                return {'error': 'No games found. Did you change your profile visibility to public?'}
            if "game_count" in steam_data and steam_data["game_count"] < 1:
                return {'error': 'No games found. Do you even have any?'}
            game_count = 0
            for game in steam_data['games']:
                if game["playtime_forever"] > 0:
                    game_count += 1
            if game_count < 1:
                return {'error': 'No games found. Is your games\' playtime private?'}            
            return steam_data
            
        steam_data = fetch_steam_data(steam_id)
        if "error" not in steam_data:
            steam_data = clean_user_data(steam_data)


    return render(request, 'index.html', {
        'steam_id': steam_id,
        'nickname': nickname,
        'steam_data': steam_data
    })