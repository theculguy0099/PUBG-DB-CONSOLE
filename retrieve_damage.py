import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


 
def option_23():
                        
                "This is to retrieve all guns which have damage greater than a particular value"
                '''
                        Take the following as input
                        Damage\n 
                '''
                try:
                    row={}
                    Damage=input("Enter Damage ")
                    query="SELECT * from Weapons WHERE Weapons.Damage > '"+Damage+"'"
                    print(query)
                    cur.execute(query)
                    print("Weapon_ID\tWeapon_Name\tAmmo\tFire_Rate\tDamage\tExtension_ID")
                    for row in cur:
                        print(str(row['Weapon_ID'])+"\t"+str(row['Weapon_Name'])+"\t"+str(row['Ammo'])+"\t"+str(row['Fire_Rate'])+"\t"+str(row['Damage'])+"\t"+str(row['Extension_ID']))
                except Exception as e:
                            con.rollback()
                            print("Failed to fetch from database")
                            print(">>>>>>>>>>>>>", e)   