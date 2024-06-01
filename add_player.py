import pymysql
import subprocess as sp
import pymysql.cursors
import redis 

from mysqlcursor import cur,con

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def option_1():
    "This is to insert players information into the database"
    '''take the following as input
        Name of the Player\n
        player_id of the Player\n
        Date_of_birth of the Player\n
        Region of the Player\n
    
    '''
    try:
        row={}
        Player_ID=input("Enter Player's ID ")
        Name=input("Enter Player's name ")
        Date_of_Birth=input("Enter Player's DOB in YYYY-MM-DD ")
        Region=input("Enter the Region of the Player ")
        Age=int(input("Enter age of the Player "))
        
        # Check if player data exists in Redis cache
        player_key = f"player:{Player_ID}"
        if redis_client.exists(player_key):
            print("Player data found in cache:")
            player_data = redis_client.hgetall(player_key)
            print(player_data)
        else:
            query="INSERT into Player(Player_ID,Name,Date_of_Birth,Region,Age)"
            query+=" values(%s, %s, %s, %s, %s)"
            cur.execute(query, (Player_ID, Name, Date_of_Birth, Region, Age))
            con.commit()
            print("Inserted into database")
            
            # Cache player data in Redis for future use
            player_data = {
                'Player_ID': Player_ID,
                'Name': Name,
                'Date_of_Birth': Date_of_Birth,
                'Region': Region,
                'Age': Age
            }
            redis_client.hmset(player_key, player_data)
            print("Player data cached in Redis")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)