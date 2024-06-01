import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con
import redis

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_player_details(player_id):
    # Check if player details exist in Redis cache
    player_key = f"player:{player_id}"
    if redis_client.exists(player_key):
        print("Player details found in cache:")
        player_data = redis_client.hgetall(player_key)
        print(player_data)
    else:
        try:
            query = f"SELECT * FROM Player WHERE Player_ID = '{player_id}'"
            cur.execute(query)
            player_data = cur.fetchone()

            if player_data:
                print("Player details retrieved from database:")
                print(player_data)

                # Cache player details in Redis
                redis_client.hmset(player_key, player_data)
                print("Player details cached in Redis")
            else:
                print("Player details not found")

        except Exception as e:
            print("Failed to fetch player details from database")
            print(">>>>>>>>>>>>>", e)

def option_27():
    "This is to update Player Player_ID"
    try:
        player_id = input("Enter Player ID: ")
        new_player_id = input("Enter New Player ID: ")
        query = f"UPDATE Player SET Player_ID = '{new_player_id}' WHERE Player_ID = '{player_id}'"
        print(query)
        cur.execute(query)
        con.commit()
        print("Updated in database")

        # Update cached player details in Redis if exists
        player_key = f"player:{player_id}"
        if redis_client.exists(player_key):
            redis_client.hset(player_key, "Player_ID", new_player_id)
            print("Updated cached player details in Redis")

    except Exception as e:
        con.rollback()
        print("Failed to update in database")
        print(">>>>>>>>>>>>>", e)

    # Call function to fetch and display updated player details
    get_player_details(new_player_id)
