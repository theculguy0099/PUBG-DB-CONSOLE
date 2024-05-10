import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_8():
    
    "This is to delete a Map from the database"

    '''take the following as input
        Map_ID\n
    '''

    try:
        row={}
        Map_ID=input("Enter Map ID ")
        query="DELETE from Maps where Map_ID='"+Map_ID+"'"
        print(query)
        cur.execute(query)
        con.commit()
        print("Deleted from database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
