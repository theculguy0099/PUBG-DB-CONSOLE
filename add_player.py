import pymysql
import subprocess as sp
import pymysql.cursors

from mysqlcursor import cur,con

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
        query="INSERT into Player(Player_ID,Name,Date_of_Birth,Region,Age)"
        query+=" values('"+Player_ID+"','"+Name+"','"+Date_of_Birth+"','"+Region+"','"+str(Age)+"')"
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
