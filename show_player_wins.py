import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_17():
    "This is to show Player(s) with highest Total-Wins"
    try:
        row = {}

        # Check if the result is cached in Redis
        cache_key = "players_with_highest_total_wins"
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            query = """
            SELECT * 
            FROM Player 
            WHERE Total_Wins = (SELECT MAX(Total_Wins) FROM Player)
            """
            cur.execute(query)
            print("Player_ID\tName\tDate_of_Birth\tRegion\tAge\tTotal_Matches_Played\tTotal_Wins\tWin_Rate")
            for row in cur:
                player_info = f"{row['Player_ID']}\t{row['Name']}\t{row['Date_of_Birth']}\t{row['Region']}\t{row['Age']}\t{row['Total_Matches_Played']}\t{row['Total_Wins']}\t{row['Win_Rate']}"
                print(player_info)

            # Cache the result in Redis
            if row:
                redis_client.hmset(cache_key, {"result": player_info})
                print("Data cached in Redis")
            else:
                print("No players found")

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

# Call the function to test
option_17()
