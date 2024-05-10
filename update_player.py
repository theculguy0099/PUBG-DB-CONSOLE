import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_27():
                                                        
    "This is to update Player Player_ID"
    '''
            Take the following as input
            Player_ID\n 
    '''
    try:
        row={}
        Player_ID=input("Enter Player ID ")
        New_Player_ID=input("Enter New Player ID ")
        query="UPDATE Player set Player_ID='"+New_Player_ID+"' where Player_ID='"+Player_ID+"'"
        print(query)
        cur.execute(query)
        con.commit()
        
        print("Updated in database")
    except Exception as e:
                con.rollback()
                print("Failed to update in database")
                print(">>>>>>>>>>>>>", e)

