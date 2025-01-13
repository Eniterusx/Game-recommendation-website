import pandas as pd
import pickle
import numpy as np
from .steam_recommender import generate_recommendations

def l2_normalize(x):
    l2_norm = np.linalg.norm(x, ord=2)
    if l2_norm == 0:
        return x
    return x / l2_norm

def clean_user_data(steam_data):
    game_data = pd.read_csv("game_data.csv")
    num_games = len(game_data)
    user_vector = np.zeros(num_games)
    for item in steam_data["games"]:
        if item["playtime_forever"] > 0 and item["appid"] in game_data["game_steam_id"].values:
            item_steam_id = item["appid"]
            game_id = game_data[game_data["game_steam_id"] == item_steam_id]["game_id"].values[0]
            user_vector[game_id] = item["playtime_forever"]
    # normalize vector
    user_data = l2_normalize(user_vector)
    # find top games played by user
    top_games_user = np.argsort(user_data)[::-1][:10]
    top_game_names = [game_data["game_name"].values[x] for x in top_games_user]
    top_game_playtimes = [round(user_vector[x] / 60, 1) for x in top_games_user]
    most_played_games = {}
    for i in range(len(top_game_names)):
        most_played_games[i] = {"name": top_game_names[i], "playtime": top_game_playtimes[i]}
    recommendations = generate_recommendations(user_data)
    # get recommendation ids and extract the game names
    recommendation_game_ids = [game_data["game_id"].values[x] for x in recommendations]
    recommendation_game_names = [game_data["game_name"].values[x] for x in recommendation_game_ids]
    recommendation_game_steam_ids = [game_data["game_steam_id"].values[x] for x in recommendation_game_ids]
    recommendation_dict = {}
    for i in range(len(recommendation_game_names)):
        recommendation_dict[i] = {"name": recommendation_game_names[i], "steam_id": recommendation_game_steam_ids[i]}
    return {
        "most_played_games": most_played_games,
        "recommendations": recommendation_dict
    }