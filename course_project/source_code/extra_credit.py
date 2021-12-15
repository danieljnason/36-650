# generate graphics for extra credit problems using seaborn library
# requires that the SQL table has been set up and highest improvement function has been run
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import pytest
import pandas as pd
import psycopg2 as pg
import pandas.io.sql as psql
conn = pg.connect(host="*****", # change to your computer's local host
                  port="*****", # change to your computer's local port
                  user="postgres",
                  password="*****", # change to your computer's password
                  database="postgres",
                  options="-c search_path=fifa")

fifa = psql.read_sql("SELECT * FROM fifa.players_20", conn)
conn.close()

# question 1
def highest_improvement(x = 10):
    """
    This function accepts a non-negative integer input "x" and returns a DataFrame object
    of the top "x" players with the highest skill improvements in descending order and their names.
    
    This is calculated by first creating the "avg_skills" column which is the average of a player's skills across specific columns that are defined by the
    FIFA 20 video game. Then, an additional column is created to calculate a player's skill improvements, which is defined to be
    the difference between a given player's average skills and the average of all players' average skils in the data set. 
    These metrics range from the skill "attack_crossing" to "goalkeeping_positioning", which are skills defined in the FIFA 20 videogame that impact a performance of a player.
    
    If no input is provided when the function is called, the default value of the "x" argument is 10, so the players with the
    top 10 highest improvement scores will be returned.
    
    The function checks that the fifa dataframe is present and the function receives a non-negative integer value input not less than 0. If this is not received,
    the function will print a message telling the user to check inputs and make sure they are the appropriate data type.
    """
    if (not isinstance(fifa, pd.DataFrame)):
        print("The FIFA dataset has not been defined in Python as a DataFrame.")
    elif (not isinstance(x, int)):
        print("Invalid input, please enter an integer value.")
    elif (x < 0):
        print("Invalid input, please enter a non-negative integer value.")
    else:
        fifa['avg_skills'] = fifa.loc[:,'attacking_crossing':'goalkeeping_positioning'].mean(axis = 1)
        fifa['skill_improvements'] = fifa['avg_skills'] - fifa['avg_skills'].mean()
        return fifa[['short_name', 'skill_improvements']].sort_values('skill_improvements', ascending=False).head(x)

# extra credit question 1 - plot players based on improvement metric
# requires highest improvement function
def graph_highest_improvement(n = 10):
    x = highest_improvement(n)
    fig, ax = plt.subplots(figsize = (10, n))
    sns.barplot(x = 'short_name', y = 'skill_improvements', data = x, ax = ax)
    ax.set_xlabel('Name of Player')
    ax.set_xticklabels(x.short_name, rotation = 40)
    ax.set_ylabel('Skill Improvement Score')
    ax.set_title('Barplot of Skill Improvement Score for the Top ' + str(n) + ' Players')
    plt.show()
    
# extra credit question 2
def graph_highest_value(n = 5):
    x = fifa[['short_name', 'value_eur']].sort_values('value_eur', ascending=False).head(n)
    fig, ax = plt.subplots(figsize = (10, n))
    sns.barplot(x = 'short_name', y = 'value_eur', data = x, ax = ax)
    ax.set_xlabel('Name of Player')
    ax.set_ylabel('Value of Player (in Hunrders of Millions of Euros)')
    ax.set_title('Barplot of Player Value for the Top ' + str(n) + ' Players')
    plt.show()
    
# extra credit question 3
def graph_greatest_number_of_traits(n = 10):
    df = fifa
    df['count_traits'] = df['player_traits'].str.count(',') + 1
    df = df.sort_values(['count_traits'], ascending=False)
    i = 0
    count = 0
    while i < len(df):
        count += 1
        if df.iloc[i, df.columns.get_loc("count_traits")] > df.iloc[i + 1, df.columns.get_loc("count_traits")] and count >= n:
            break
        i += 1
    df = df[['short_name', 'count_traits']].head(count) # or df.iloc[:count, :]

    fig, ax = plt.subplots(figsize=(10,count/2))
    sns.barplot(y = 'short_name', x = 'count_traits', orient = 'h', data = df,  ax = ax)
    ax.set_ylabel('Name of Player')
    ax.set_xlabel('Count of Player Traits')
    ax.set_title('Barplot of the ' + str(n) + ' Players with the Highest Count of Traits (including ties)')
    plt.show()
