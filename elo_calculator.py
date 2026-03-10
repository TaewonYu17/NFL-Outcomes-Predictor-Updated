from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

BASE_RATING = 1500
K = 20
HOME_FIELD_ADVANTAGE = 65

def calculate_expected_result(elo_team, elo_opp, HorA):
    # Example implementation, adjust as needed
    return 1 / (1 + 10 ** ((elo_opp + HorA - elo_team) / 400))

def calculate_mov_multiplier(point_diff, elo_diff):
    # Example implementation, adjust as needed
    try:
        if point_diff + 1 <= 0:
            return 0
        denominator = elo_diff * 0.001 + 2.2
        if abs(denominator) < 1e-10:
            return 0
        return np.log(point_diff + 1) * (2.2 / denominator)
    except Exception:
        return 0

def calculate_elo(nfl_data, base_rating=BASE_RATING, k=K, home_field_advantage=HOME_FIELD_ADVANTAGE):
    elo_ratings = {}
    history = []

    for index, row in nfl_data.iterrows():
        team = row['Team']
        opp = row['Opp']
        week = row['Week']
        year = row['Year']
        point_diff = row['PD']
        HorA = row['HorA']

        elo_team = elo_ratings.get(team, base_rating)
        elo_opp = elo_ratings.get(opp, base_rating)

        if week == 1:
            elo_team += 0
            elo_opp += 0  # placeholder for offseason moves

        if HorA == -1:
            home_field = home_field_advantage
        else:
            home_field = -home_field_advantage

        expected_result = calculate_expected_result(elo_team, elo_opp, HorA)
        mov_multiplier = calculate_mov_multiplier(point_diff, elo_team - elo_opp)

        if point_diff > 0:
            score = 1
        elif point_diff < 0:
            score = 0
        else:
            score = 0.5

        elo_change = k * (score - expected_result) * mov_multiplier

        elo_ratings[team] = elo_team + elo_change
        elo_ratings[opp] = elo_opp - elo_change

        history.append({
            'Date': row['Date'],
            'Team': team,
            'Opp': opp,
            'Team_Elo': elo_ratings[team],
            'Opp_Elo': elo_ratings[opp],
        })

    return pd.DataFrame(history)

@app.route('/calculate_elo', methods=['POST'])
def calculate_elo_api():
    data = request.get_json()
    nfl_data = pd.DataFrame(data)
    elo_df = calculate_elo(nfl_data)
    return elo_df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
