import pandas as pd
import matplotlib.pyplot as plt

 # remove games that last longer than 35 minutes (2100 seconds)
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # clean games where no team got a dragon
    no_dragon = df[df['firstDragon'] != 0]
    no_baron = no_dragon[no_dragon['gameDuration'] < 2100]
    return no_baron

# calculate number of wins for each team
def calc_wins(df: pd.DataFrame) -> list[int]:
    blue_dragon = df[(df['firstDragon'] == 1) & (df['winner'] == 1)].count()
    blue_no_dragon = df[(df['firstDragon'] == 2) & (df['winner'] == 1)].count()
    red_dragon = df[(df['firstDragon'] == 2) & (df['winner'] == 2)].count()
    red_no_dragon = df[(df['firstDragon'] == 1) & (df['winner'] == 2)].count()
    return [blue_no_dragon['gameId'], red_no_dragon['gameId'], blue_dragon['gameId'], red_dragon['gameId']]

def create_graph(total_games, data):
    categories = ['Blue', 'Red', 'Blue + Dragon', 'Red + Dragon']
    plt.bar(categories, data, color=['#1F8BFF', '#FF4E50', '#1F8BFF', '#FF4E50'])
    plt.xlabel(f'Total Games: {total_games}')
    plt.title('Winrate with/without First Dragon')

    # add percentage labels
    for i, value in enumerate(data):
        pct = (value / total_games) * 100
        plt.text(i, value, f'{pct:.1f}%', ha='center', va='bottom')
    plt.show()


def main():
    # create pandas DataFrame
    df = pd.read_csv('./league_data.csv')
    # clean the data
    cleaned = clean_data(df)
    total_games = cleaned.count()['gameId']
    # fetch winrates with/without first dragon
    data = calc_wins(cleaned)
    # plot the graph
    create_graph(total_games, data)

if __name__ == '__main__':
    main()
