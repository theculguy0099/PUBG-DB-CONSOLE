import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_5():
    "This is to insert Team Information into the database"

    '''take the following as input
        Team_ID\n
        Player_ID1\n
        Player_ID2\n
        Player_ID3\n
        Player_ID4\n
        '''    

    try:
        row={}
        Team_ID=input("Enter Team ID ")
        Player_ID1=input("Enter Player ID 1 ")
        Player_ID2=input("Enter Player ID 2 ")
        Player_ID3=input("Enter Player ID 3 ")
        Player_ID4=input("Enter Player ID 4 ")
        query="INSERT into Team(Team_ID,Player_ID1,Player_ID2,Player_ID3,Player_ID4)"
        query+=" values('"+Team_ID+"','"+Player_ID1+"','"+Player_ID2+"','"+Player_ID3+"','"+Player_ID4+"')"
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
