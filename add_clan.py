import pymysql
import subprocess as sp
import pymysql.cursors
import redis

from mysqlcursor import cur, con

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_4():
    "This is to insert clans information into the database"

    '''take the following as input
        Clan_ID\n
        Clan_Name\n
        ClanLeader_ID\n
    '''

    try:
        row = {}
        Clan_ID = input("Enter Clan ID ")
        Clan_Name = input("Enter Clan Name ")
        ClanLeader_ID = input("Enter Clan Leader ID ")
        
        # Check if clan data exists in Redis cache
        clan_key = f"clan:{Clan_ID}"
        if redis_client.exists(clan_key):
            print("Clan data found in cache:")
            clan_data = redis_client.hgetall(clan_key)
            print(clan_data)
        else:
            query = "INSERT into Clans(Clan_ID,Clan_Name,ClanLeader_ID)"
            query += " values(%s, %s, %s)"
            cur.execute(query, (Clan_ID, Clan_Name, ClanLeader_ID))
            con.commit()

            # Update MemberOf table
            query1 = "INSERT into MemberOf(Player_ID,Clan_ID)"
            query1 += " values(%s, %s)"
            cur.execute(query1, (ClanLeader_ID, Clan_ID))
            con.commit()

            print("Inserted into database")

            # Cache clan data in Redis for future use
            clan_data = {
                'Clan_ID': Clan_ID,
                'Clan_Name': Clan_Name,
                'ClanLeader_ID': ClanLeader_ID
            }
            redis_client.hmset(clan_key, clan_data)
            print("Clan data cached in Redis")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
