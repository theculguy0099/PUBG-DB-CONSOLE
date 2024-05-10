import pymysql
import subprocess as sp
import pymysql.cursors
from mysqlcursor import cur,con


def option_10():

    "This is to update Clan-Leader of a Clan in the Game"

    '''take the following as input
        Clan_ID\n
        ClanLeader_ID\n
    '''

    try:
        row={}
        Clan_ID=input("Enter Clan ID ")
        ClanLeader_ID=input("Enter Clan Leader ID ")
        query="UPDATE Clans set ClanLeader_ID='"+ClanLeader_ID+"' where Clan_ID='"+Clan_ID+"'"
        print(query)
        cur.execute(query)
        con.commit()
        print("Updated in database")

    except Exception as e:
        con.rollback()
        print("Failed to update in database")
        print(">>>>>>>>>>>>>", e)

