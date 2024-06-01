import pymysql
import redis
from mysqlcursor import cur, con

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_2():
    "This is to insert maps information into the database"

    '''take the following as input
        Map_ID\n
        Map_Name\n
        Map_Dimension\n
        Terrain\n
    '''

    try:
        row = {}
        Map_ID = input("Enter Map ID: ")
        Map_Name = input("Enter Map Name: ")
        Map_Dimension = input("Enter Map Dimension: ")
        Terrain = input("Enter Terrain: ")

        # Check if map data exists in Redis cache
        map_key = f"map:{Map_ID}"
        if redis_client.exists(map_key):
            print("Map data found in cache:")
            map_data = redis_client.hgetall(map_key)
            print(map_data)
        else:
            # Insert data into MySQL
            query = "INSERT INTO Maps(Map_ID, Map_Name, Map_Dimension, Terrain) VALUES (%s, %s, %s, %s)"
            cur.execute(query, (Map_ID, Map_Name, Map_Dimension, Terrain))
            con.commit()
            print("Inserted into database")

            # Cache map data in Redis
            map_data = {
                'Map_Name': Map_Name,
                'Map_Dimension': Map_Dimension,
                'Terrain': Terrain
            }
            redis_client.hmset(map_key, map_data)
            print("Map data cached in Redis")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


