# main.py
# This is your code's starting point
# Follow the guidelines in the homework document
# Don't forget to add data folder for your data
# importing with sql
import pandas as pd
import psycopg2 as pg
import pandas.io.sql as psql

conn = pg.connect(host="****", # this information should be from your local host
                  port="****", # this information should be from your local host
                  user="postgres",
                  password="****", # this information should be from your local host
                  database="postgres",
                  options="-c search_path=fifa") # this information should be from your local host, requires schema "fifa"

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

# unit testing
def test_highest_improvement_happy_path():
    assert len(highest_improvement()) == 10, "Length of results should be 10 if no argument is passed to the function."
    assert len(highest_improvement(5)) == 5, "Length of results should be 5."
    assert isinstance(highest_improvement(), pd.DataFrame), "Return type should be a DataFrame."
    
def test_highest_improvement_sad_path():
    assert len(highest_improvement(10000000000)) == 10000000000, "Output returned by function is a list but should not be."
    assert type(highest_improvement(-1)) is None, "Output returned by function is not None type but should be."
    assert type(highest_improvement(5.5)) is None, "Output returned by function is not None type but should be."

# question 2
def players_contract_year_2021(y = 10):
    """
    This function accepts a non-negative integer input "y" and returns a DataFrame object of the top "y" clubs with the 
    largest number of players with contracts ending in 2021. 
    
    This is achieved by filtering the fifa DataFrame rows to when
    year is 2021 and grouping the players by club and then counting the number of players who satisfy the condition for a 
    given club and sorting the clubs in descending order.
    
    If no input is provided when the function is called, the default value of the "y" argument is 10, so the
    10 clubs with the most number of players with contracts ending in 2021 are returned.
    
    The function checks that the fifa dataframe is present and the function receives a non-negative integer value input not less than 0. If this is not received,
    the function will print a message telling the user to check inputs and make sure they are the appropriate data type.
    """
    if (not isinstance(fifa, pd.DataFrame)):
        print("The FIFA dataset has not been defined in Python as a DataFrame.")
    elif (not isinstance(y, int)):
        print("Invalid input, please enter an integer value.")
    elif (y < 0):
        print("Invalid input, please enter a non-negative integer value.")
    else:
        q2 = fifa[fifa['contract_valid_until'] == 2021].groupby('club')["sofifa_id"].count().sort_values(ascending=False)
        return q2.head(y)

# testing question 2
def test_players_contract_year_2021_happy_path():
    assert len(players_contract_year_2021()) == 10, "Length of results should be 10 if no argument is passed to the function."
    assert len(players_contract_year_2021(5)) == 5, "Length of results should be 5."
    assert isinstance(players_contract_year_2021(), pd.DataFrame), "Return type should be a DataFrame."

def test_players_contract_year_2021_sad_path():
    assert len(players_contract_year_2021(10000000000)) == 10000000000, "Output returned by function is a list but should not be."
    assert type(players_contract_year_2021(-1)) is None, "Output returned by function is not None type but should be."
    assert type(players_contract_year_2021(5.5)) is None, "Output returned by function is not None type but should be."

# question 3
def largest_clubs(z = 10):
    """
    This function accepts a non-negative integer input "z" greater than or equal to 5 and returns a DataFrame object of the
    top "z" clubs with the largest number of players. 
    
    This is achieved by grouping the rows of the fifa DataFrame by club and then counting the number of players
    for a given club and sorting the clubs in descending order.
    
    If no input is provided when the function is called, the default value of the "z" argument is 10, so the
    10 clubs with the most number of players are returned, where z is greater than 5.
    
    The function checks that the fifa dataframe is present and the function receives a non-negative integer value input not less than 5. If this is not received,
    the function will print a message telling the user to check inputs and make sure they are the appropriate data type.
    """
    if (not isinstance(fifa, pd.DataFrame)):
        print("The FIFA dataset has not been defined in Python as a DataFrame.")
    elif (not isinstance(z, int)):
        print("Invalid input, please enter an integer value.")
    elif (z < 5):
        print("Invalid input, please enter a non-negative integer value.")
    else:
        q3 = fifa.groupby('club')["sofifa_id"].count().sort_values(ascending=False)
        return q3.head(z)

# unit testing question 3
def test_highest_improvement_happy_path():
    assert len(largest_clubs()) == 10, "Length of results should be 10 if no argument is passed to the function."
    assert len(largest_clubs(20)) == 20, "Length of results should be 20."
    assert isinstance(largest_clubs(), pd.DataFrame), "Return type should be a DataFrame."
    
def test_highest_improvement_sad_path():
    assert len(largest_clubs(10000000000)) == 10000000000, "Output returned by function is a list but should not be."
    assert type(largest_clubs(-1)) is None, "Output returned by function is not None type but should be."
    assert type(largest_clubs(5.5)) is None, "Output returned by function is not None type but should be."
    assert type(largest_clubs(4)) is None, "Output returned by function is not None type but should be."

# question 4
# most popular nation
def most_popular_nation_position(x = 1):
    """
    This function accepts a non-negative integer input "x" and returns a DataFrame object of the "x" most popular nation
    positions, excluding "SUB" (substitute) and "RES" (reserve) since these are not real positions for a soccer team but
    included in the FIFA dataset to track players that are on a team but not actively playing. 
    
    This is achieved by filter rows of the fifa DataFrame to exclude reserve and substitute positions and storing this in a
    new DataFrame. This new "clean" DataFrame is then grouped by nation position and then the counts of these positions are
    sorted in descending order.
    
    If no input is provided when the function is called, the default value of the "x" argument is 1, so the
    most popular nation position is returned.
    
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
        clean_fifa = fifa[(fifa['nation_position'] != "SUB") & (fifa['nation_position'] != "RES")]
        q4a = clean_fifa.groupby('nation_position')["sofifa_id"].count().sort_values(ascending=False)
        return q4a.head(x)

# unit testing for most popular nation position
def test_highest_improvement_happy_path():
    assert len(most_popular_nation_position()) == 10, "Length of results should be 10 if no argument is passed to the function."
    assert len(most_popular_nation_position(20)) == 20, "Length of results should be 20."
    assert isinstance(most_popular_nation_position(), pd.DataFrame), "Return type should be a DataFrame."

def test_highest_improvement_sad_path():
    assert len(most_popular_nation_position(10000000000)) == 10000000000, "Output returned by function is a list but should not be."
    assert type(most_popular_nation_position(-1)) is None, "Output returned by function is not None type but should be."
    assert type(most_popular_nation_position(5.5)) is None, "Output returned by function is not None type but should be."

# most popular team position
def most_popular_team_position(x = 1):
    """
    This function accepts a non-negative integer input "x" and returns a DataFrame object of the "x" most popular team
    positions, excluding "SUB" (substitute) and "RES" (reserve) since these are not real positions for a soccer team but
    included in the FIFA dataset to track players that are on a team but not actively playing. 
    
    This is achieved by filter rows of the fifa DataFrame to exclude reserve and substitute positions and storing this in a
    new DataFrame. This new "clean" DataFrame is then grouped by team position and then the counts of these positions are
    sorted in descending order.
    
    If no input is provided when the function is called, the default value of the "x" argument is 1, so the
    most popular team position is returned.
    
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
        clean_fifa = fifa[(fifa['team_position'] != "SUB") & (fifa['team_position'] != "RES")]
        q4b = clean_fifa.groupby('team_position')["sofifa_id"].count().sort_values(ascending=False)
        return q4b.head(x)

# unit testing for most popular nation position
def test_highest_improvement_happy_path():
    assert len(most_popular_team_position()) == 10, "Length of results should be 10 if no argument is passed to the function."
    assert len(most_popular_team_position(20)) == 20, "Length of results should be 20."
    assert isinstance(most_popular_team_position(), pd.DataFrame), "Return type should be a DataFrame."

def test_highest_improvement_sad_path():
    assert len(most_popular_team_position(10000000000)) == 10000000000, "Output returned by function is a list but should not be."
    assert type(most_popular_team_position(-1)) is None, "Output returned by function is not None type but should be."
    assert type(most_popular_team_position(5.5)) is None, "Output returned by function is not None type but should be."

# question 5 - most popular nationality
def most_popular_nationality(x = 1):
    """
    This function accepts a non-negative integer input "x" and returns a DataFrame object of the "x" most popular nationality. 
    
    This is achieved by grouping the rows of the fifa DataFrame by nationality and then counting the number of players
    for a given nationality and sorting the nationalities in descending order.
    
    If no input is provided when the function is called, the default value of the "x" argument is 1, so the
    most popular nationality is returned.
    
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
        q5 = fifa.groupby('nationality')["sofifa_id"].count().sort_values(ascending=False)
        return q5.head(x)

# unit testing for most popular nation position
def test_highest_improvement_happy_path():
    assert len(most_popular_nationality()) == 10, "Length of results should be 10 if no argument is passed to the function."
    assert len(most_popular_nationality(20)) == 20, "Length of results should be 20."
    assert isinstance(most_popular_nationality(), pd.DataFrame), "Return type should be a DataFrame."

def test_highest_improvement_sad_path():
    assert len(most_popular_nationality(10000000000)) == 10000000000, "Output returned by function is a list but should not be."
    assert type(most_popular_nationality(-1)) is None, "Output returned by function is not None type but should be."
    assert type(most_popular_nationality(5.5)) is None, "Output returned by function is not None type but should be."
