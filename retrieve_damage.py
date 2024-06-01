import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_23():
    "This is to retrieve all guns which have damage greater than a particular value"
    '''
        Take the following as input
        Damage\n 
    '''
    try:
        Damage = input("Enter Damage: ")
        # Create a unique cache key for this query
        cache_key = f"weapons:damage_gt:{Damage}"

        # Check if the result is cached in Redis
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            print("Weapon_ID\tWeapon_Name\tAmmo\tFire_Rate\tDamage\tExtension_ID")
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            # SQL query to find weapons with damage greater than the specified value
            query = """
            SELECT Weapon_ID, Weapon_Name, Ammo, Fire_Rate, Damage, Extension_ID
            FROM Weapons
            WHERE Damage > %s
            """
            cur.execute(query, (Damage,))
            weapons = cur.fetchall()

            if weapons:
                print("Weapon_ID\tWeapon_Name\tAmmo\tFire_Rate\tDamage\tExtension_ID")
                weapon_data = {}
                for idx, row in enumerate(weapons):
                    weapon_str = f"{row['Weapon_ID']}\t{row['Weapon_Name']}\t{row['Ammo']}\t{row['Fire_Rate']}\t{row['Damage']}\t{row['Extension_ID']}"
                    print(weapon_str)
                    weapon_data[f"weapon_{idx}"] = weapon_str

                # Cache the result in Redis
                redis_client.hmset(cache_key, weapon_data)
                print("Data cached in Redis")
            else:
                print("No weapons found with damage greater than", Damage)

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)


