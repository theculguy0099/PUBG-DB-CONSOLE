import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_16():
    "This is to show Team(s) with highest Win-Rate"
    try:
        row = {}

        # Check if the result is cached in Redis
        cache_key = "teams_with_highest_win_rate"
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            query = """
            SELECT * 
            FROM Team 
            WHERE Win_Rate = (SELECT MAX(Win_Rate) FROM Team)
            """
            cur.execute(query)
            print("Team_ID\tPlayer_ID1\tPlayer_ID2\tPlayer_ID3\tPlayer_ID4\tNumber_Of_Matches_Played\tWins\tWin_Rate")
            for row in cur:
                team_info = f"{row['Team_ID']}\t{row['Player_ID1']}\t{row['Player_ID2']}\t{row['Player_ID3']}\t{row['Player_ID4']}\t{row['Number_Of_Matches_Played']}\t{row['Wins']}\t{row['Win_Rate']}"
                print(team_info)

            # Cache the result in Redis
            if row:
                redis_client.hmset(cache_key, {"result": team_info})
                print("Data cached in Redis")
            else:
                print("No teams found")

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)
