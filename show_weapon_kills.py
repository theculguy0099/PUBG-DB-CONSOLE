import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con

def option_19():
    
        "This is to output the Weapon with Most Kills "
    
        try:
            # row={}
    
            query="SELECT * from Weapons where Weapon_ID in (select Weapon_ID from Kills group by Weapon_ID order by count(Weapon_ID) desc) limit 1"
            print(query)
            cur.execute(query)
            print("Weapon_ID\tWeapon_Name\tAmmo\tFire_Rate\tDamage\tExtension_ID")
            for row in cur:
                print(str(row['Weapon_ID'])+"\t"+str(row['Weapon_Name'])+"\t"+str(row['Ammo'])+"\t"+str(row['Fire_Rate'])+"\t"+str(row['Damage'])+"\t"+str(row['Extension_ID']))




        except Exception as e:
            con.rollback()
            print("Failed to fetch from database")
            print(">>>>>>>>>>>>>", e)

