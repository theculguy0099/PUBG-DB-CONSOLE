import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_24():
    "This is to retrieve top gun for a particular player"
    '''
        Take the following as input
        Player_ID\n or 
        Name\n
    '''
    try:
        row = {}
        Player_ID = input("Enter Player ID: ")
        cache_key = f"top_gun_for_player:{Player_ID}"

        # Check if the result is cached in Redis
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            query = """
            SELECT Player.Name, Weapons.Weapon_Name, COUNT(*) AS weapon_count
            FROM Player
            JOIN Kills ON Kills.Player_ID_killer = Player.Player_ID
            JOIN Weapons ON Weapons.Weapon_ID = Kills.Weapon_ID
            WHERE Player.Player_ID = %s
            GROUP BY Weapons.Weapon_ID
            ORDER BY weapon_count DESC
            LIMIT 1
            """
            cur.execute(query, (Player_ID,))
            top_gun = cur.fetchone()

            if top_gun:
                result_str = f"{top_gun['Name']}\t{top_gun['Weapon_Name']}\t{top_gun['weapon_count']}"
                print("Name\tWeapon_Name\tCOUNT(Weapon_ID)")
                print(result_str)

                # Cache the result in Redis
                redis_client.hmset(cache_key, {"result": result_str})
                print("Data cached in Redis")
            else:
                print("No top gun found for the given player")

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

