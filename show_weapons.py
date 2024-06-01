import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_12():
    "This is to show the list of all Weapons in Game"
    try:
        row = {}

        # Check if the result is cached in Redis
        cache_key = "all_weapons_in_game"
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            query = "SELECT * FROM Weapons"
            cur.execute(query)
            print("Weapon_ID\tWeapon_Name\tAmmo\tFire_Rate\tDamage\tExtension_ID")
            for row in cur:
                weapon_info = f"{row['Weapon_ID']}\t{row['Weapon_Name']}\t{row['Ammo']}\t{row['Fire_Rate']}\t{row['Damage']}\t{row['Extension_ID']}"
                print(weapon_info)

            # Cache the result in Redis
            if row:
                redis_client.hmset(cache_key, {"result": weapon_info})
                print("Data cached in Redis")
            else:
                print("No weapons found")

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

