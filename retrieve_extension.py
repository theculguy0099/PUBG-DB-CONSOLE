import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_22():
    "This is to retrieve extension for a particular gun"
    '''
        Take the following as input
        Weapon_name\n 
    '''
    try:
        Weapon_Name = input("Enter Weapon Name: ")
        # Create a unique cache key for this query
        cache_key = f"weapon_extension:{Weapon_Name}"

        # Check if the result is cached in Redis
        if redis_client.exists(cache_key):
            print("Data found in cache:")
            cached_data = redis_client.hgetall(cache_key)
            print("Extension_ID\tSCOPE\tMAG\tGRIP")
            for key, value in cached_data.items():
                print(value.decode('utf-8'))
        else:
            # SQL query to find extension details for the given weapon name
            query = """
            SELECT Extension.Extension_ID, Extension.SCOPE, Extension.MAG, Extension.GRIP
            FROM Extension
            JOIN Weapons ON Weapons.Extension_ID = Extension.Extension_ID
            WHERE Weapons.Weapon_Name = %s
            """
            cur.execute(query, (Weapon_Name,))
            extensions = cur.fetchall()

            if extensions:
                print("Extension_ID\tSCOPE\tMAG\tGRIP")
                extension_data = {}
                for idx, row in enumerate(extensions):
                    extension_str = f"{row['Extension_ID']}\t{row['SCOPE']}\t{row['MAG']}\t{row['GRIP']}"
                    print(extension_str)
                    extension_data[f"extension_{idx}"] = extension_str

                # Cache the result in Redis
                redis_client.hmset(cache_key, extension_data)
                print("Data cached in Redis")
            else:
                print("No extensions found for the given weapon name")

        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

