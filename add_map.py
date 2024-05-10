import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con

def option_2():

    "This is to insert maps information into the database"
    '''take the following as input
        Map_ID\n
        Map_Name\n
        Map_Dimension\n
        Terrain\n
    '''

    try:
        row={}
        Map_ID=input("Enter Map ID ")
        Map_Name=input("Enter Map Name ")
        Map_Dimension=input("Enter Map Dimension ")
        Terrain=input("Enter Terrain ")
        query="INSERT into Maps(Map_ID,Map_Name,Map_Dimension,Terrain)"
        query+=" values('"+Map_ID+"','"+Map_Name+"','"+Map_Dimension+"','"+Terrain+"')"
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
