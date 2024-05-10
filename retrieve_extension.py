import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_22():
                
        "This is to retrieve extension for a particular gun"
        '''
                Take the following as input
                Weapon_name\n 
        '''
        try:
            row={}
            Weapon_ID=input("Enter Weapon ID ")
            query="SELECT * from Extension JOIN Weapons on Weapons.Extension_ID=Extension.Extension_ID WHERE Weapons.Weapon_Name='"+Weapon_ID+"'"
            print(query)
            cur.execute(query)
            print("Extension_ID\tSCOPE\tMAG\tGRIP")
            for row in cur:
                print(str(row['Extension_ID'])+"\t"+str(row['SCOPE'])+"\t"+str(row['MAG'])+"\t"+str(row['GRIP']))
        except Exception as e:
                    con.rollback()
                    print("Failed to fetch from database")
                    print(">>>>>>>>>>>>>", e)  