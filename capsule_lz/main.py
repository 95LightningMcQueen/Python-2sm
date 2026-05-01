import os
from logger import log_decorator
from stats import GraphicalStatistics


@log_decorator
def start_lab():
    file_name = 'playstation_players.csv'
    if os.path.exists(file_name):
        visual = GraphicalStatistics(file_name)
        visual.make_chart()
    else:
        print(f'File {file_name} not found')

if __name__ == "__main__":
    start_lab()
