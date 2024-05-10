import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_11():
    
    "This is to show the list of all Maps in Game"

    try:
        row={}
        query="SELECT * from Maps"
        print(query)
        cur.execute(query)
        print("Map_ID\tMap_Name\tMap_Dimension\tTerrain")
        for row in cur:
            print(str(row['Map_ID'])+"\t"+row['Map_Name']+"\t"+row['Map_Dimension']+"\t"+row['Terrain'])

    except Exception as e:
        con.rollback()
        print("Failed to fetch from database")
        print(">>>>>>>>>>>>>", e)



def option_20():
        
            "This is to output the list of all game maps"
        
            try:
                row={}
                query="SELECT * from Maps"
                print(query)
                cur.execute(query)
                print("Map_ID\tMap_Name\tMap_Dimension\tTerrain")
                for row in cur:
                    print(str(row['Map_ID'])+"\t"+row['Map_Name']+"\t"+row['Map_Dimension']+"\t"+row['Terrain'])
        
            except Exception as e:
                con.rollback()
                print("Failed to fetch from database")
                print(">>>>>>>>>>>>>", e)
