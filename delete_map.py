import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_8():
    "This is to delete a Map from the database"

    '''take the following as input
        Map_ID\n
    '''

    try:
        Map_ID = input("Enter Map ID: ")

        # Check if map data exists in Redis cache
        map_key = f"map:{Map_ID}"
        if redis_client.exists(map_key):
            redis_client.delete(map_key)
            print("Map data removed from Redis cache")

        query = "DELETE FROM Maps WHERE Map_ID = %s"
        cur.execute(query, (Map_ID,))
        con.commit()
        print("Deleted from database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

