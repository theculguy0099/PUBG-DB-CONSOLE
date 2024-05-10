import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_24():
                                    
    "This is to retrieve top gun for a particular player"
    '''
            Take the following as input
            Player_ID\n or 
            Name\n
    '''
    try:
        row={}
        Player_ID=input("Enter Player ID ")
        query="SELECT Name,Weapons.Weapon_Name,COUNT(*) from Player JOIN Kills on Kills.Player_ID_killer=Player.Player_ID"+" JOIN Weapons on Weapons.Weapon_ID=Kills.Weapon_ID"+" WHERE Player_ID = '"+Player_ID+"' "+" GROUP BY Weapons.Weapon_ID ORDER BY COUNT(*) DESC LIMIT 1"
        print(query)
        print("Name\tWeapon_Name\tCOUNT(Weapon_ID)")
        cur.execute(query)
        for row in cur:
            print(str(row['Name'])+"\t"+str(row['Weapon_Name'])+"\t"+str(row['COUNT(*)']))
    except Exception as e:
                con.rollback()
                print("Failed to fetch from database")
                print(">>>>>>>>>>>>>", e)
            #WHAT DO I NEED TO DO IN BELOW FUNCTION
   