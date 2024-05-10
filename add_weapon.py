import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con

def option_3():
    "This is to insert weapons information into the database"

    '''take the following as input
        Weapon_ID\n
        Weapon_Name\n
        Ammo\n
        Fire_Rate\n
        Damage\n
        Extension_ID\n
    '''

    try:
        row={}
        Weapon_ID=input("Enter Weapon ID ")
        Weapon_Name=input("Enter Weapon Name ")
        Ammo=input("Enter Ammo ")
        Fire_Rate=input("Enter Fire Rate ")
        Damage=input("Enter Damage ")
        Extension_ID=input("Enter Extension ID ")
        query="INSERT into Weapons(Weapon_ID,Weapon_Name,Ammo,Fire_Rate,Damage,Extension_ID)"
        query+=" values('"+Weapon_ID+"','"+Weapon_Name+"','"+Ammo+"','"+Fire_Rate+"','"+Damage+"','"+Extension_ID+"')"
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
