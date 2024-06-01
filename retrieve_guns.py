import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_21():
    "This is to retrieve guns for a particular extension"
    '''
        Take the following as input
        SCOPE\n 
        Or MAG\n 
        Or GRIP\n
    '''
    try:
        row = {}
        Extension_ID = input("Enter Extension ID: ")
        cache_key = f"guns_for_extension:{Extension_ID}"

        # Check if the result is cached in Redis
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            print("Weapon_ID\tWeapon_Name\tAmmo\tFire_Rate\tDamage\tExtension_ID")
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            query = """
            SELECT Weapons.Weapon_ID, Weapons.Weapon_Name, Weapons.Ammo, Weapons.Fire_Rate, Weapons.Damage, Weapons.Extension_ID 
            FROM Weapons 
            JOIN Extension ON Weapons.Extension_ID = Extension.Extension_ID 
            WHERE Extension.SCOPE = %s OR Extension.MAG = %s OR Extension.GRIP = %s
            """
            cur.execute(query, (Extension_ID, Extension_ID, Extension_ID))
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
                print("No guns found for the given extension")

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

