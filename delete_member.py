import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_9():
    
    "This is to delete a Player from a Clan from the database"

    '''take the following as input
        Player_ID\n
        Clan_ID\n
    '''

    try:
        row={}
        Player_ID=input("Enter Player ID ")
        Clan_ID=input("Enter Clan ID ")
        query="DELETE from MemberOf where Player_ID='"+Player_ID+"' and Clan_ID='"+Clan_ID+"'"
        print(query)
        cur.execute(query)
        con.commit()
        print("Deleted from database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

