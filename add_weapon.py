import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_3():
    "This is to insert weapons information into the database"

    '''take the following as input
        Weapon_ID\n
        Weapon_Name\n
        Ammo\n
        Fire_Rate\n
        Damage\n
        Extension_ID\n
    '''

    try:
        Weapon_ID = input("Enter Weapon ID: ")
        Weapon_Name = input("Enter Weapon Name: ")
        Ammo = input("Enter Ammo: ")
        Fire_Rate = input("Enter Fire Rate: ")
        Damage = input("Enter Damage: ")
        Extension_ID = input("Enter Extension ID: ")

        # Check if weapon data exists in Redis cache
        weapon_key = f"weapon:{Weapon_ID}"
        if redis_client.exists(weapon_key):
            print("Weapon data found in cache:")
            weapon_data = redis_client.hgetall(weapon_key)
            print({k.decode('utf-8'): v.decode('utf-8') for k, v in weapon_data.items()})
        else:
            query = "INSERT INTO Weapons(Weapon_ID, Weapon_Name, Ammo, Fire_Rate, Damage, Extension_ID) VALUES (%s, %s, %s, %s, %s, %s)"
            cur.execute(query, (Weapon_ID, Weapon_Name, Ammo, Fire_Rate, Damage, Extension_ID))
            print("Inserted into Weapons table")

            # Cache weapon data in Redis
            weapon_data = {
                'Weapon_Name': Weapon_Name,
                'Ammo': Ammo,
                'Fire_Rate': Fire_Rate,
                'Damage': Damage,
                'Extension_ID': Extension_ID
            }
            redis_client.hmset(weapon_key, weapon_data)
            print("Weapon data cached in Redis")

        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

