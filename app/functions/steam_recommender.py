import numpy as np
import gc

def recommend_for_user(new_user_vector, user_game_matrix, num_neighbors=5, games=20):
    similarities = np.dot(user_game_matrix, new_user_vector)
    similar_user_list = np.argsort(similarities)

    # if the score is higher than 0.999, it means the user is the same as the new user
    # so we will remove this user from the list
    similar_user_list = similar_user_list[similarities[similar_user_list] < 0.999]
    top_similar_users = similar_user_list[-num_neighbors:]

    # calc total playtime of each game by all top_similar_users
    game_scores = np.sum(user_game_matrix[top_similar_users], axis=0)

    # remove games that the new user has already played
    new_user_played_games = np.where(new_user_vector > 0)[0]
    game_scores[new_user_played_games] = 0

    # get top k longest playtime games
    recommended_games = np.argsort(game_scores)[-games:][::-1]

    return recommended_games[:games]


def generate_recommendations(user_data):
    num_neighbors = 5
    games_rec = 25

    user_game_matrix = np.load("user_matrix.npz")["matrix"]

    recommended_games = recommend_for_user(
        new_user_vector=user_data,
        user_game_matrix=user_game_matrix,
        num_neighbors=num_neighbors,
        games=games_rec)
    
    del user_game_matrix
    gc.collect()

    return recommended_games