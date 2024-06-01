import pymysql
import subprocess as sp
import pymysql.cursors
import redis
from mysqlcursor import cur, con

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_11():
    "This is to show the list of all Maps in Game"
    try:
        # Check if maps data exists in Redis cache
        maps_key = "maps"
        # if redis_client.exists(maps_key):
        #     print("Maps data found in cache:")
        #     maps_data = redis_client.get(maps_key)
        #     print(maps_data.decode())  # Decode bytes to string
        # else:
        row = {}
        query = "SELECT * FROM Maps"
        # print(query)
        cur.execute(query)
        maps_data = []
        print("Map_ID\tMap_Name\tMap_Dimension\tTerrain")
        for row in cur:
            map_info = f"{row['Map_ID']}\t{row['Map_Name']}\t{row['Map_Dimension']}\t{row['Terrain']}"
            print(map_info)
            maps_data.append(map_info)
            # Cache maps data in Redis for future use
        redis_client.set(maps_key, "\n".join(maps_data))
        print("Maps data cached in Redis")
    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

def option_20():
    "This is to output the list of all game maps"
    try:
        # Check if maps data exists in Redis cache
        maps_key = "maps"
        if redis_client.exists(maps_key):
            print("Maps data found in cache:")
            maps_data = redis_client.get(maps_key)
            print(maps_data.decode())  # Decode bytes to string
        else:
            row = {}
            query = "SELECT * FROM Maps"
            print(query)
            cur.execute(query)
            maps_data = []
            print("Map_ID\tMap_Name\tMap_Dimension\tTerrain")
            for row in cur:
                map_info = f"{row['Map_ID']}\t{row['Map_Name']}\t{row['Map_Dimension']}\t{row['Terrain']}"
                print(map_info)
                maps_data.append(map_info)
            # Cache maps data in Redis for future use
            redis_client.set(maps_key, "\n".join(maps_data))
            print("Maps data cached in Redis")
    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)
