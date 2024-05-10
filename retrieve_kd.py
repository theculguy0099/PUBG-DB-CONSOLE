import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con

def option_26():
                                                    
                "This is to retrieve all Players having KD>=x"
                '''
                        Take the following as input
                        KD\n 
                '''
                try:
                    row={}
                    KD=input("Enter KD ")
                    query="SELECT Name,COUNT(*),Player.Total_Matches_Played as k1 from Player"+" JOIN Kills ON Kills.Player_ID_killer = Player.Player_ID GROUP BY Player.Player_ID HAVING "+KD+"*k1<=COUNT(*)"
                    print(query)
                    cur.execute(query)
                    for row in cur:
                        print(str(row['Name'])+"\t"+str(row['COUNT(*)']))
                    # print("Name\tKD")
                except Exception as e:
                            con.rollback()
                            print("Failed to fetch from database")
                            print(">>>>>>>>>>>>>", e)