import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_25():
    "This is to retrieve best team members for a particular player"
    '''
        Take the following as input
        Player_ID\n or 
        Name\n
    '''
    try:
        Player_ID = input("Enter Player ID: ")
        # Create a unique cache key for this query
        cache_key = f"best_team:{Player_ID}"

        # Check if the result is cached in Redis
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            # SQL query to find the best team members for the given player
            query = """
            SELECT Player_ID1, Player_ID2, Player_ID3, Player_ID4
            FROM Team
            JOIN Player ON Player_ID = Team.Player_ID1 
                       OR Player_ID = Team.Player_ID2 
                       OR Player_ID = Team.Player_ID3 
                       OR Player_ID = Team.Player_ID4
            WHERE Player_ID = %s
            ORDER BY Team.Win_Rate DESC 
            LIMIT 1
            """
            cur.execute(query, (Player_ID,))
            row = cur.fetchone()
            if row:
                player_ids = [str(row['Player_ID1']), str(row['Player_ID2']), str(row['Player_ID3']), str(row['Player_ID4'])]
                print("\t".join(player_ids))

                # Cache the result in Redis
                redis_client.hmset(cache_key, {f"Player_ID{i+1}": player_id for i, player_id in enumerate(player_ids)})
                print("Data cached in Redis")
            else:
                print("No data found for the given Player ID")

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)


