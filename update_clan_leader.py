import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_10():
    "This is to update Clan-Leader of a Clan in the Game"
    try:
        row = {}

        # Input Clan_ID and ClanLeader_ID
        Clan_ID = input("Enter Clan ID: ")
        ClanLeader_ID = input("Enter Clan Leader ID: ")

        # Execute the update query
        query = f"UPDATE Clans SET ClanLeader_ID = '{ClanLeader_ID}' WHERE Clan_ID = '{Clan_ID}'"
        cur.execute(query)
        con.commit()
        print("Updated in database")

        # Invalidate cache for the updated Clan ID
        cache_key = f"clan:{Clan_ID}"
        if redis_client.exists(cache_key):
            redis_client.delete(cache_key)
            print("Cache invalidated for Clan ID:", Clan_ID)

    except Exception as e:
        con.rollback()
        print("Failed to update in database")
        print(">>>>>>>>>>>>>", e)
