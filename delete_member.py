import pymysql
import redis
from mysqlcursor import cur, con

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_9():
    "This is to delete a Player from a Clan from the database"

    '''take the following as input
        Player_ID\n
        Clan_ID\n
    '''

    try:
        Player_ID = input("Enter Player ID: ")
        Clan_ID = input("Enter Clan ID: ")

        # Check if player-clan relationship exists in Redis cache
        player_clan_key = f"player_clan:{Player_ID}:{Clan_ID}"
        if redis_client.exists(player_clan_key):
            redis_client.delete(player_clan_key)
            print("Player-Clan relationship removed from Redis cache")

        query = "DELETE FROM MemberOf WHERE Player_ID = %s AND Clan_ID = %s"
        cur.execute(query, (Player_ID, Clan_ID))
        con.commit()
        print("Deleted from database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
