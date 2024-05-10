import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con



def option_21():
            
    "This is to retrieve guns for a particular extension"
    '''
            Take the following as input
            SCOPE\n 
            Or MAG\n 
            Or GRIP\n
    '''
    try:
        row={}
        Extension_ID=input("Enter Extension ID ")
        query="SELECT * from Weapons JOIN Extension on Weapons.Extension_ID=Extension.Extension_ID WHERE Extension.SCOPE='"+Extension_ID+"' OR Extension.MAG='"+Extension_ID+"' OR Extension.GRIP='"+Extension_ID+"'"
        print(query)
        cur.execute(query)
        print("Weapon_ID\tWeapon_Name\tAmmo\tFire_Rate\tDamage\tExtension_ID")
        for row in cur:
            print(str(row['Weapon_ID'])+"\t"+str(row['Weapon_Name'])+"\t"+str(row['Ammo'])+"\t"+str(row['Fire_Rate'])+"\t"+str(row['Damage'])+"\t"+str(row['Extension_ID']))
    except Exception as e:
                con.rollback()
                print("Failed to fetch from database")
                print(">>>>>>>>>>>>>", e)