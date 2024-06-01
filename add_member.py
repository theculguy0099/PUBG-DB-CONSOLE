import pymysql
import redis
from mysqlcursor import cur, con

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_7():
    "This is to insert Player to Clan Information into the database"

    '''take the following as input
        Player_ID\n
        Clan_ID\n
    '''

    try:
        Player_ID = input("Enter Player ID: ")
        Clan_ID = input("Enter Clan ID: ")

        # Check if player-clan association exists in Redis cache
        player_clan_key = f"player_clan:{Player_ID}:{Clan_ID}"
        if redis_client.exists(player_clan_key):
            print("Player to Clan association found in cache.")
            player_clan_data = redis_client.hgetall(player_clan_key)
            print(player_clan_data)
        else:
            query = "INSERT INTO MemberOf(Player_ID, Clan_ID) VALUES (%s, %s)"
            cur.execute(query, (Player_ID, Clan_ID))
            print("Inserted into MemberOf table")

            # Cache player-clan association in Redis
            player_clan_data = {
                'Player_ID': Player_ID,
                'Clan_ID': Clan_ID
            }
            redis_client.hmset(player_clan_key, player_clan_data)
            print("Player to Clan association cached in Redis")

        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
