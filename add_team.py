import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_5():
    "This is to insert Team Information into the database"

    '''take the following as input
        Team_ID\n
        Player_ID1\n
        Player_ID2\n
        Player_ID3\n
        Player_ID4\n
    '''    

    try:
        Team_ID = input("Enter Team ID: ")
        Player_ID1 = input("Enter Player ID 1: ")
        Player_ID2 = input("Enter Player ID 2: ")
        Player_ID3 = input("Enter Player ID 3: ")
        Player_ID4 = input("Enter Player ID 4: ")

        # Check if team data exists in Redis cache
        team_key = f"team:{Team_ID}"
        if redis_client.exists(team_key):
            print("Team data found in cache:")
            team_data = redis_client.hgetall(team_key)
            print({k.decode('utf-8'): v.decode('utf-8') for k, v in team_data.items()})
        else:
            query = "INSERT INTO Team(Team_ID, Player_ID1, Player_ID2, Player_ID3, Player_ID4) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, (Team_ID, Player_ID1, Player_ID2, Player_ID3, Player_ID4))
            print("Inserted into Team table")

            # Cache team data in Redis
            team_data = {
                'Player_ID1': Player_ID1,
                'Player_ID2': Player_ID2,
                'Player_ID3': Player_ID3,
                'Player_ID4': Player_ID4
            }
            redis_client.hmset(team_key, team_data)
            print("Team data cached in Redis")

        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


