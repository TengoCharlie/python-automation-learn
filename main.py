# Read CSV from URl using pandas and download all the files on website

import pandas as pd
# Read 1 csv frm website
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

# showing dataframes
df_premier21

#rename columns
df_premier21.rename(columns={'FTHG': 'home_goals','FTAG': 'away_goals'}, inplace=True)
print(df_premier21)