import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con



def option_18():

    "This is to show List of Player(s) a player has Team-UP with"

    '''Take the following as input
        Player_ID\n
    '''

    try:
        row={}
        Player_ID=input("Enter Player ID ")
        query="select Name,Team.Team_ID from Player JOIN Team on Player_ID=Team.Player_ID1 OR Player_ID=Team.Player_ID2 OR Player_ID=Team.Player_ID3 OR Player_ID=Team.Player_ID4 where Team.Player_ID1='"+Player_ID+"'" +"OR Team.Player_ID2='"+Player_ID+"'" +"OR Team.Player_ID3='"+Player_ID+"'" +"OR Team.Player_ID4='"+Player_ID+"'"
        print(query)
        cur.execute(query)
        print("Name\t Team_ID\t")
        for row in cur:
            print(str(row['Name'])+"\t"+str(row['Team_ID']))

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

