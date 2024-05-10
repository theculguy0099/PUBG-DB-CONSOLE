import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con

def option_12():
        
    "This is to show the list of all Weapons in Game"

    try:
        row={}
        query="SELECT * from Weapons"
        print(query)
        cur.execute(query)
        
        print("Weapon_ID\tWeapon_Name\tAmmo\tFire_Rate\tDamage\tExtension_ID")
        for row in cur:
            print(str(row['Weapon_ID'])+"\t"+row['Weapon_Name']+"\t"+str(row['Ammo'])+"\t"+str(row['Fire_Rate'])+"\t"+str(row['Damage'])+"\t"+str(row['Extension_ID']))

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)

