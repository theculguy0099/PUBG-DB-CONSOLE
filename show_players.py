import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_13():
        
    "This is to show the list of all Players in Game"

    try:
        row={}
        query="SELECT * from Player"
        print(query)
        cur.execute(query)
        print("Player_ID\tName\tDate_of_Birth\tRegion\tAge")
        for row in cur:
            print(str(row['Player_ID'])+"\t"+row['Name']+"\t"+str(row['Date_of_Birth'])+"\t"+row['Region']+"\t"+str(row['Age']))

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

