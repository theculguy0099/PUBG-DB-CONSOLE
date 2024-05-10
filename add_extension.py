import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_6():
    "This is to insert Extension Information into the database"

    '''take the following as input
        Extension_ID\n
        SCOPE\n
        MAG\n
        GRIP\n
    '''

    try:
        row={}
        Extension_ID=input("Enter Extension ID ")
        SCOPE=input("Enter SCOPE ")
        MAG=input("Enter MAG ")
        GRIP=input("Enter GRIP ")
        query="INSERT into Extension(Extension_ID,SCOPE,MAG,GRIP)"
        query+=" values('"+Extension_ID+"','"+SCOPE+"','"+MAG+"','"+GRIP+"')"
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
