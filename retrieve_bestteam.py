import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con

   
def option_25():
                                            
        "This is to retrieve best team members for a particular player"
        '''
                Take the following as input
                Player_ID\n or 
                Name\n
        '''
        try:
            row={}
            Player_ID=input("Enter Player ID")
            query="SELECT Player_ID1,Player_ID2,Player_ID3,Player_ID4 from Team JOIN Player ON Player_ID=Team.Player_ID1  OR Player_ID=Team.Player_ID2 OR Player_ID=Team.Player_ID3 OR Player_ID=Team.Player_ID4 ORDER BY Team.Win_Rate DESC LIMIT 1"
            print(query)
            cur.execute(query)
            for row in cur:
                print(str(row['Player_ID1'])+"\t"+str(row['Player_ID2'])+"\t"+str(row['Player_ID3'])+"\t"+str(row['Player_ID4']))
            # for row in cur:
            #     print(str(row['P1.Name==='])+"\t"+str(row['P2.Name'])+"\t"+str(row['P3.Name'])+"\t"+str(row['P4.Name']))
            # print("Name1\tName2\tName3\tName4")
        except Exception as e:
                    con.rollback()
                    print("Failed to fetch from database")
                    print(">>>>>>>>>>>>>", e)   
