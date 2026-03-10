# NFL Outcome Predictor

This project predicts NFL game outcomes using ELO ratings and machine learning. It is designed to handle both past games (with available stats) and future games (without stats), providing a flexible and robust approach to NFL game prediction.

## Features
- Calculates ELO ratings for NFL teams based on historical game results
- Performs feature engineering and rolling averages for team statistics
- Trains a Random Forest classifier to predict game outcomes
- Handles predictions for both past and future games
- Visualizes prediction results and model performance

## Project Structure
- `nfl_game_predictor.ipynb`: Main notebook for data processing, ELO calculation, model training, and prediction
- `elo_calculator.py`: ELO calculation logic (if used separately)
- `nfl_schedule_stats_2020_2025.csv`: NFL schedule and stats data
- `nfl_schedule_results_2019_2023.csv`: Historical NFL results
- `nfl_webscraper.ipynb`: Notebook for scraping NFL data (if needed)
- `README.md`: Project documentation

## Getting Started
1. **Clone the repository**
   ```sh
   git clone git@github.com:TaewonYu17/NFL-Outcomes-Predictor-Updated.git
   cd NFL-Outcomes-Predictor-Updated
   ```
2. **Set up a Python virtual environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the notebook**
   Open `nfl_game_predictor.ipynb` in VS Code or Jupyter and follow the steps.

## Usage
- Update the CSV files with the latest NFL data as needed.
- Run the notebook cells in order to process data, calculate ELO ratings, train the model, and generate predictions.

## Requirements
- Python 3.8+
- pandas, numpy, scikit-learn, jupyter, matplotlib (see `requirements.txt`)

## License
This project is licensed under the MIT License.

## Author
Taewon Yu
