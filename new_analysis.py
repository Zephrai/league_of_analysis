import pandas as pd
import matplotlib.pyplot as plt

 # remove games where neither team got any baron kills
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # clean games where no team got a dragon
    clean_df = df[df['team0DragonFirst'] ^ df['team1DragonFirst']]

    no_baron = clean_df[(clean_df['team0BaronKills'] == 0) & (clean_df['team1BaronKills'] == 0)]
    return no_baron

# calculate number of wins for each team
def calc_wins(df: pd.DataFrame) -> list[int]:
    blue_win = len(df[(df['team0DragonFirst'] == False) & (df['team0Win'] == True)])
    red_win = len(df[(df['team1DragonFirst'] == False) & (df['team1Win'] == True)])
    blue_first_dragon = len(df[(df['team0DragonFirst'] == True) & (df['team0Win'] == True)])
    red_first_dragon =  len(df[(df['team1DragonFirst'] == True) & (df['team1Win'] == True)])
    return [blue_win, red_win, blue_first_dragon, red_first_dragon]

def create_graph(total_games: int, data: list[int]) -> None:
    categories = ['Blue', 'Red', 'Blue + Dragon', 'Red + Dragon']
    plt.bar(categories, data, color=['#1F8BFF', '#FF4E50', '#1F8BFF', '#FF4E50'])
    plt.xlabel(f'Total Games: {total_games}')
    plt.title('Winrate with/without First Dragon')

    # add percentage labels
    for i, value in enumerate(data):
        pct = (value / total_games) * 100
        plt.text(i, value, f'{pct:.1f}%', ha='center', va='bottom')
    plt.show()


def main() -> None:
    # create pandas DataFrame
    df = pd.read_csv('./new_data.csv')
    # clean the data
    cleaned = clean_data(df)
    total_games = len(cleaned)
    # fetch winrates with/without first dragon
    data = calc_wins(cleaned)
    # plot the graph
    create_graph(total_games, data)

if __name__ == '__main__':
    main()