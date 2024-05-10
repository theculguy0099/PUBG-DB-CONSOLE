import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_17():

    "This is to show Player(s) with highest Total-Wins"

    try:
        row={}
        query="SELECT * from Player where Total_Wins=(select max(Total_Wins) from Player)"
        print(query)
        cur.execute(query)
        print("Player_ID\tName\tDate_of_Birth\tRegion\tAge\tTotal_Matches_Played\tTotal_Wins\tWin_Rate")
        for row in cur:
            print(str(row['Player_ID'])+"\t"+row['Name']+"\t"+str(row['Date_of_Birth'])+"\t"+row['Region']+"\t"+str(row['Age'])+"\t"+str(row['Total_Matches_Played'])+"\t"+str(row['Total_Wins'])+"\t"+str(row['Win_Rate']))

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)
