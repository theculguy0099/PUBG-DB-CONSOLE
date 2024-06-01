import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_26():
    "This is to retrieve all Players having KD>=x"
    '''
        Take the following as input
        KD\n 
    '''
    try:
        row = {}
        KD = input("Enter KD: ")
        cache_key = f"players_with_kd_gte:{KD}"

        # Check if the result is cached in Redis
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            query = """
            SELECT Name, COUNT(*) AS kill_count, Player.Total_Matches_Played as total_matches 
            FROM Player
            JOIN Kills ON Kills.Player_ID_killer = Player.Player_ID 
            GROUP BY Player.Player_ID 
            HAVING %s * total_matches <= COUNT(*)
            """
            cur.execute(query, (KD,))
            players = cur.fetchall()

            if players:
                player_data = {}
                for idx, row in enumerate(players):
                    player_str = f"{row['Name']}\t{row['kill_count']}"
                    print(player_str)
                    player_data[f"player_{idx}"] = player_str

                # Cache the result in Redis
                redis_client.hmset(cache_key, player_data)
                print("Data cached in Redis")
            else:
                print("No players found with KD >= " + KD)

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

