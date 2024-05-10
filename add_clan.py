import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_4():
    "This is to insert clans information into the database"

    '''take the following as input
        Clan_ID\n
        Clan_Name\n
        ClanLeader_ID\n
    '''

    try:
        row={}
        Clan_ID=input("Enter Clan ID ")
        Clan_Name=input("Enter Clan Name ")
        ClanLeader_ID=input("Enter Clan Leader ID ")
        query="INSERT into Clans(Clan_ID,Clan_Name,ClanLeader_ID)"
        query+=" values('"+Clan_ID+"','"+Clan_Name+"','"+ClanLeader_ID+"')"
        print(query)
        cur.execute(query)
        con.commit()

        # update MemberOf table
        query1="INSERT into MemberOf(Player_ID,Clan_ID)"
        query1+=" values('"+ClanLeader_ID+"','"+Clan_ID+"')"
        print(query1)
        cur.execute(query1)
        con.commit()


        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

