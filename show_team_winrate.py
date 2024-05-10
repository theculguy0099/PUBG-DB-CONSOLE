import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con



def option_16():

    "This is to show Team(s) with highest Win-Rate"

    try:
        row={}
        query="SELECT * from Team where Win_Rate=(select max(Win_Rate) from Team)"
        print(query)
        cur.execute(query)
        print("Team_ID\tPlayer_ID1\tPlayer_ID2\tPlayer_ID3\tPlayer_ID4\tNumber_Of_Matches_Played\tWins\tWin_Rate")
        for row in cur:
            print(str(row['Team_ID'])+"\t"+str(row['Player_ID1'])+"\t"+str(row['Player_ID2'])+"\t"+str(row['Player_ID3'])+"\t"+str(row['Player_ID4'])+"\t"+str(row['Number_Of_Matches_Played'])+"\t"+str(row['Wins'])+"\t"+str(row['Win_Rate']))

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)
