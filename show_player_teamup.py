import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_18():

    "This is to show List of Player(s) a player has Team-UP with"

    '''Take the following as input
        Player_ID\n
    '''

    try:
        row = {}
        Player_ID = input("Enter Player ID: ")
        cache_key = f"teammates_for_player:{Player_ID}"

        # Check if the result is cached in Redis
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            query = """
            SELECT Name, Team.Team_ID
            FROM Player 
            JOIN Team 
            ON Player.Player_ID = Team.Player_ID1 
            OR Player.Player_ID = Team.Player_ID2 
            OR Player.Player_ID = Team.Player_ID3 
            OR Player.Player_ID = Team.Player_ID4 
            WHERE Team.Player_ID1 = %s 
            OR Team.Player_ID2 = %s 
            OR Team.Player_ID3 = %s 
            OR Team.Player_ID4 = %s
            """
            cur.execute(query, (Player_ID, Player_ID, Player_ID, Player_ID))
            teammates = cur.fetchall()

            if teammates:
                print("Name\t Team_ID\t")
                teammates_data = {}
                for idx, row in enumerate(teammates):
                    teammate_str = f"{row['Name']}\t{row['Team_ID']}"
                    print(teammate_str)
                    teammates_data[f"teammate_{idx}"] = teammate_str

                # Cache the result in Redis
                redis_client.hmset(cache_key, teammates_data)
                print("Data cached in Redis")
            else:
                print("No teammates found for the given player")

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

