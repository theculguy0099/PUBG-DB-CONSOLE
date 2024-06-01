import pymysql
import redis
from mysqlcursor import cur, con

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_6():
    "This is to insert Extension Information into the database"

    '''take the following as input
        Extension_ID\n
        SCOPE\n
        MAG\n
        GRIP\n
    '''

    try:
        row = {}
        Extension_ID = input("Enter Extension ID: ")
        SCOPE = input("Enter SCOPE: ")
        MAG = input("Enter MAG: ")
        GRIP = input("Enter GRIP: ")

        # Check if extension data exists in Redis cache
        extension_key = f"extension:{Extension_ID}"
        if redis_client.exists(extension_key):
            print("Extension data found in cache:")
            extension_data = redis_client.hgetall(extension_key)
            print(extension_data)
        else:
            # Insert data into MySQL
            query = "INSERT INTO Extension(Extension_ID, SCOPE, MAG, GRIP) VALUES (%s, %s, %s, %s)"
            cur.execute(query, (Extension_ID, SCOPE, MAG, GRIP))
            con.commit()
            print("Inserted into database")

            # Cache extension data in Redis
            extension_data = {
                'SCOPE': SCOPE,
                'MAG': MAG,
                'GRIP': GRIP
            }
            redis_client.hmset(extension_key, extension_data)
            print("Extension data cached in Redis")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

