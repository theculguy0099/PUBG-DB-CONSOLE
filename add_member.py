import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con



def option_7():

    "This is to insert Player to Clan Information into the database"

    '''take the following as input
        Player_ID\n
        Clan_ID\n
    '''

    try:
        row={}
        Player_ID=input("Enter Player ID ")
        Clan_ID=input("Enter Clan ID ")
        query="INSERT into MemberOf(Player_ID,Clan_ID)"
        query+=" values('"+Player_ID+"','"+Clan_ID+"')"
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

