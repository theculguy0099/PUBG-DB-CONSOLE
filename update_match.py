import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur, con
import redis

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_15():
    "This is to update Match Details of Game after it has ended"
    try:
        row = {}
        Match_ID = input("Enter Match ID: ")
        Winnner_Team_ID = input("Enter Winner Team ID: ")
        query = f"UPDATE Matches SET Winner_Team_ID='{Winnner_Team_ID}' WHERE Match_ID='{Match_ID}'"
        cur.execute(query)

        # Update number of wins of the team
        query = f"UPDATE Team SET Wins=Wins+1 WHERE Team_ID='{Winnner_Team_ID}'"
        cur.execute(query)

        # Update win rate of the team
        query = f"UPDATE Team SET Win_Rate=Wins/Number_Of_Matches_Played WHERE Team_ID='{Winnner_Team_ID}'"
        cur.execute(query)

        # Update number of wins of the players in the winning team
        query = f"UPDATE Player SET Total_Wins=Total_Wins+1 WHERE Player_ID IN (SELECT Player_ID1 FROM Team WHERE Team_ID='{Winnner_Team_ID}')"
        cur.execute(query)
        query = f"UPDATE Player SET Total_Wins=Total_Wins+1 WHERE Player_ID IN (SELECT Player_ID2 FROM Team WHERE Team_ID='{Winnner_Team_ID}')"
        cur.execute(query)
        query = f"UPDATE Player SET Total_Wins=Total_Wins+1 WHERE Player_ID IN (SELECT Player_ID3 FROM Team WHERE Team_ID='{Winnner_Team_ID}')"
        cur.execute(query)
        query = f"UPDATE Player SET Total_Wins=Total_Wins+1 WHERE Player_ID IN (SELECT Player_ID4 FROM Team WHERE Team_ID='{Winnner_Team_ID}')"
        cur.execute(query)

        # Update win rate of the players in the winning team
        query = f"UPDATE Player SET Win_Rate=Total_Wins/Total_Matches_Played WHERE Player_ID IN (SELECT Player_ID1 FROM Team WHERE Team_ID='{Winnner_Team_ID}')"
        cur.execute(query)
        query = f"UPDATE Player SET Win_Rate=Total_Wins/Total_Matches_Played WHERE Player_ID IN (SELECT Player_ID2 FROM Team WHERE Team_ID='{Winnner_Team_ID}')"
        cur.execute(query)
        query = f"UPDATE Player SET Win_Rate=Total_Wins/Total_Matches_Played WHERE Player_ID IN (SELECT Player_ID3 FROM Team WHERE Team_ID='{Winnner_Team_ID}')"
        cur.execute(query)
        query = f"UPDATE Player SET Win_Rate=Total_Wins/Total_Matches_Played WHERE Player_ID IN (SELECT Player_ID4 FROM Team WHERE Team_ID='{Winnner_Team_ID}')"
        cur.execute(query)

        Number_Of_Kills = int(input("Enter Number of Kills: "))
        query = f"UPDATE Matches SET Number_Of_Kills='{Number_Of_Kills}' WHERE Match_ID='{Match_ID}'"
        cur.execute(query)

        # Insert kills
        for i in range(1, Number_Of_Kills + 1):
            Player_ID_killer = input("Enter Player ID Killer: ")
            Weapon_ID = input("Enter Weapon ID: ")
            Player_ID_killed = input("Enter Player ID Killed: ")
            query = f"INSERT INTO Kills(Match_ID, Player_ID_killer, Weapon_ID, Player_ID_killed) VALUES ('{Match_ID}', '{Player_ID_killer}', '{Weapon_ID}', '{Player_ID_killed}')"
            cur.execute(query)

        # Commit changes to the database
        con.commit()
        print("Updated in database")

        # Cache the updated match details in Redis
        cache_key = f"match:{Match_ID}"
        match_data = {
            "Match_ID": Match_ID,
            "Winner_Team_ID": Winnner_Team_ID,
            "Number_Of_Kills": Number_Of_Kills
        }
        redis_client.hmset(cache_key, match_data)
        print("Match details cached in Redis")

    except Exception as e:
        con.rollback()
        print("Failed to update in database")
        print(">>>>>>>>>>>>>", e)
